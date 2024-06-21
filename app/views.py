from django.shortcuts import render

from . models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")

def contact(request):
    if request.method=='POST':
        c=Contactform(request.POST)
        if c.is_valid():
            c.save()
            
    return render(request,"contact.html")    
def faq(request):
    return render(request,"faq.html")    
def gallery(request):
    context={}
    pld=Gallery.objects.all()
    std=Feedback.objects.all()
    ltd=Before.objects.all()
    context['pld']=pld
    context['std']=std
    context['ltd']=ltd

    return render(request,"gallery.html",context)   
def testimonials(request):
    pld=Testimonial.objects.all()
    return render(request,"testimonials.html",{'pld':pld})   
def treatment(request):
    return render(request,"treatment.html") 
def blog1(request):
    return render(request,"blog1.html")
def blog2(request):
    return render(request,"blog2.html")
def blog3(request):
    return render(request,"blog3.html")
def blog4(request):
    return render(request,"blog4.html")                      
def appoint(request):
    if request.method=='POST':
        d=Productform(request.POST)
        if d.is_valid():
            d.save()
            return index(request)    
    return render(request,'appoint.html')