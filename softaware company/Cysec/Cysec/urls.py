"""
URL configuration for Cysec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from website import views
from adminapp import views as admin_user


urlpatterns = [
    path('',views.home),
    path('about_us/',views.about_us),
    path('faqs/',views.faqs),
    path('testimonials/',views.test),
    path('our-teams/',views.our_teams),
    path('team_details/',views.team_details),
    path('event_landing_page/',views.event_landing_page),
    path('services/',views.services),
    path('service_details/',views.service_details),
    path('blog_details/',views.blog_details),
    path('authentication/',views.authentication),
    path('contact_us/',views.contact_us),
    path('forget_password/',views.forget_password),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    
    
    
    
    path('admin1/',admin_user.home),
    path('admin1/create_account/',admin_user.account),
    path('admin1/save_account/',admin_user.save_account),
    path('admin1/login/',admin_user.admin_login),
    path("admin1/save_login/",admin_user.save_login),
    path('admin1/logout/',admin_user.logout),
    path('admin1/slider/',admin_user.slider),
    path('admin1/save_slider/',admin_user.save_slider),
    
    
    path('admin/', admin.site.urls),
]
