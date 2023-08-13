from django.urls import path
from . import views

urlpatterns = [
    
    path('mainpage.html', views.mainpage, name='mainpage'),
    path('page1.html',views.page1, name='page1'),
    path('page2.html',views.page2, name='page2'),
    
]