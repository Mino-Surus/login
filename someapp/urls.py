from django.urls import path, include
from .views import show_number, set_number

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('number', show_number),
    path('number/set/<int:number>', set_number)
]