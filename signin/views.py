from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.


def signin(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is None:
                
                messages.info(request, "Hmm, Invalid id OR Password🧐")
                return render(request, "signin.html")
            else:
                auth.login(request, user) 
                messages.info(request, "Successfully log in🥳!")
                return redirect('/')     
        else:
            return render(request,'signin.html')