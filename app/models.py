from django.db import models

# Create your models here.
# class Product(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     phone=models.IntegerField()
#     date=models.IntegerField()
#     time=models.IntegerField()
class Booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    date=models.DateField()
    time=models.CharField(max_length=10)
    message=models.CharField(max_length=50)
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
class Testimonial(models.Model):
    name=models.CharField(max_length=50)
    review=models.CharField(max_length=100)
class Gallery(models.Model):
    image=models.CharField(max_length=3000)  
class Feedback(models.Model):
    image=models.CharField(max_length=3000)   
class Before(models.Model):
    image=models.CharField(max_length=3000)         