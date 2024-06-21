from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('appoint/',views.appoint,name='appoint'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('blog1/',views.blog1,name='blog1'),
    path('blog2/',views.blog2,name='blog2'),
    path('blog3/',views.blog3,name='blog3'),
    path('blog4/',views.blog4,name='blog4'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('gallery/',views.gallery,name='gallery'),
    path('treatment/',views.treatment,name='treatment'),
    path('testimonials/',views.testimonials,name='testimonials')
]
