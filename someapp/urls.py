from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('account/', include('django.contrib.auth.urls')),
    path('cabinet/', views.cabinet_view, name='cabinet'),  
]