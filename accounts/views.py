from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth ,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import  CreateUserForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib import auth

def registerPage(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST) 
		if form.is_valid():
			user = form.save(commit=False) 
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your AAI account'
			message = render_to_string('acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
			   	'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			email.send()
			messages.success(request, 'Plaese Verify your Account!')
			return redirect("login")
	else:
		form = CreateUserForm()
		context = {'form':form }
		return render(request, 'signup.html', context)
	
			#return redirect('login')	
	

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		messages.success(request, 'Successfully verified!')
		return redirect("login")
	else:
		return HttpResponse('Activation link is invalid!')	
			
def loginPage(request):
	#if request.user.is_authenticated:
	#	return redirect('login')
	#else:
	if request.method == 'POST':
		u = request.POST['Username']
		p =request.POST['Password']

		user = authenticate(request, username=u, password=p)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/')			
			else:
				messages.info(request, 'Username OR password is incorrect')
	  
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

#class SignUp(generic.CreateView):
#    form_class = UserCreationForm
 #   success_url = reverse_lazy('login.html')
  #  template_name = 'signup.html'