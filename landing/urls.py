from django.urls import path
from .views import * # импортирую из документо views.py все содержимое(*)

urlpatterns = [
# ПОДКЛЮЧАЮ НАШЕ ПРЕДСТАВЛЕНИЕ index из views.py
	path('', index, name='index_url'),
	path('contact-form/', emailView, name='email'),
    path('success', successView, name='success'),
]