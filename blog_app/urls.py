from django.urls import path

from blog_app import views

urlpatterns = [

    path('',views.home,name='home'),
    path('portfolio',views.portfolio,name="portfolio")

]