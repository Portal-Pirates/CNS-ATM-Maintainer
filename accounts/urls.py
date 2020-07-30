from django.urls import path
#from .views import homepage
from . import views
from django.conf.urls import url



urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	#path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
	
]

urlpatterns += [
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]



