from django.contrib import admin
from . models import *
# Register your models here.
class Product_display(admin.ModelAdmin):
    list_display=['name','email','phone','date','time','message']
admin.site.register(Booking,Product_display)
class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message']
admin.site.register(Contact,Contact_display)    
class Testimonial_display(admin.ModelAdmin):
    list_display=['name','review']
admin.site.register(Testimonial,Testimonial_display) 
class Gallery_display(admin.ModelAdmin):
    list_display=["image"]  
admin.site.register(Gallery,Gallery_display) 
class Feedback_display(admin.ModelAdmin):
    list_display=["image"]  
admin.site.register(Feedback,Feedback_display) 
class Before_display(admin.ModelAdmin):
    list_display=["image"]  
admin.site.register(Before,Before_display) 