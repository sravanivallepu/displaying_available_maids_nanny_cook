"""
URL configuration for maidbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('user_login/',user_login,name='user_login'),
    path('booking/',booking,name='booking'),
    path('registration/',registration,name='registration'),
    path('user_logout/',user_logout,name='user_logout'),
    path('display_profile/',display_profile,name='display_profile'),
    path('change_password/',change_password,name='change_password'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    path('About/',About,name='About'),
    path('Contact/',Contact,name='Contact'),
    path('nanny/',nanny,name='nanny'),
    path('maid/',maid,name='maid'),
    path('cook/',cook,name='cook'),
    path('care_taker/',care_taker,name='care_taker'),
    path('service_list/',service_list,name='service_list'),
    path('available_cooks/',available_cooks,name='available_cooks'),
    path('available_maids/',available_maids,name='available_maids') , 
    path('available_caretaker/',available_caretaker,name='available_caretaker') ,
    path('available_nanny/',available_nanny,name='available_nanny'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


