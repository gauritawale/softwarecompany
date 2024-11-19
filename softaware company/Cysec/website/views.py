from django.shortcuts import render
from website import models 
from adminapp import models as admin_models


# Create your views here.
def home(req):
    slider=admin_models.Slider.objects.get(id=3)
    feature=models.Feature.objects.all()
    obj={'slider':slider,'feature':feature}
    return render(req,'website/index.html',obj)


def about_us(req):
    return render(req,'website/about_us.html')

def contact_us(req):
    return render(req,'website/contact_us.html')

def faqs(req):
    return render(req,'website/faqs.html')

def test(req):
    return render(req,'website/test.html')

def our_teams(req):
    return render(req,'website/our_teams.html')

def team_details(req):
    return render(req,'website/team_details.html')


def event_landing_page(req):
    return render(req,'website/event_landing_page.html')

def services(req):
    return render(req,'website/services.html')

def service_details(req):
    return render(req,'website/service_details.html')

def blog_details(req):
    return render(req,'website/blog_details.html')


def authentication(req):
    return render(req,'website/authentication.html')

def forget_password(req):
    return render(req,'website/forget_password.html')
    
def cart(req):
    return render(req,'website/cart.html')

def checkout(req):
    return render(req,'website/checkout.html')
