from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminapp import models

# Create your views here.
def home(req):
    return render(req,'admin1/index.html')

def account(req):
    return render(req,'admin1/Account.html')

def save_account(req):
    
    admin=models.Account(
    admin_name=req.POST['admin_name'],
    admin_number=req.POST['admin_number'],
    admin_email=req.POST['admin_email'],
    admin_password=req.POST['admin_password'],
    
    )
    
    
    admin.save()
    return redirect('/admin1/login/')


def admin_login(req):
    return render(req,"admin1/login.html")

def save_login(req):
    # print(req.POST)   # use for print the login password and login email in CMD
    user=models.Account.objects.filter(   #use for search the email and password
        admin_email=req.POST['admin_email'],
        admin_password=req.POST['admin_password'],
                                       
        )
    if len(user)>0:
        req.session['login_id']=user[0].id  # i
        return redirect('/admin1/')
    else:
     return redirect('/admin1/login/')
 
 
def logout(req):
    del req.session['login_id']
    return redirect('/')

def slider(req):
    slider=models.Slider.objects.get(id=3)
    obj={'slider':slider}
    return render(req,'admin1/slider.html',obj)

def save_slider(req):
    
    # slider=models.Slider(
    #     slider_subtitle=req.POST['slider_subtitle'],
    #     slider_title=req.POST['slider_title'],
    #     slider_image = req.FILES['slider_image'],
    #     slider_video_link=req.POST['slider_video_link'],
    #     slider_button1=req.POST['slider_button1'],
    #     slider_button1_link=req.POST['slider_button1_link'],
    #     slider_button2=req.POST['slider_button2'],
    #     slider_button2_link=req.POST['slider_button2_link'],
    #     slider_details=req.POST['slider_details'],
    
    # )
    # slider.save()
    # return redirect('/admin1/slider/')

    
    slider=models.Slider.objects.get(id=3)
    slider.slider_subtitle=req.POST['slider_subtitle']
    slider.slider_title=req.POST['slider_title']
    slider.slider_video_link=req.POST['slider_video_link']
    slider.slider_button1=req.POST['slider_button1']
    slider.slider_button1_link=req.POST['slider_button1_link']
    slider.slider_button2=req.POST['slider_button2']
    slider.slider_button2_link=req.POST['slider_button2_link']
    slider.slider_details=req.POST['slider_details']
    
    if 'slider_image' in req.FILES:
        slider.slider_image=req.FILES['slider_image']
    slider.save()
    return redirect('/admin1/slider/')

    
    
    
   

