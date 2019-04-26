from .forms import ContactForm
from .models import Partners
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
	return render(request, 'landing/lotos_index.html')


def emailView(request):
	if request.method == 'GET': # принемаем введеные данные в форму
		form = ContactForm() 
	else:
		form = ContactForm(request.POST) # метод пост отправляет данные из формы на сервер
		if form.is_valid():# проверяем валидность введеных даных
			subject = form.cleaned_data['name'] # извлекаем из словаря cleaned_data очищенные данные name, email, message
			email = form.cleaned_data['email']
			text = form.cleaned_data['text']
			message = "Имя:%s"'\n' % subject
			message += "Email:%s"'\n' % email
			message += "Текст сообщения:%s"'\n' % text
			try:
				send_mail(subject, message, ['lotex-ecostroy@sozvezdielotos.ru'], ['lotex-ecostroy@sozvezdielotos.ru']) # отправляем письмо с именем сообщением и адресом на указаный адрес
			except BadHeaderError: # защита от уязвимости если данные не прошли отчистку или содержат вредоносный скрипт возбудить исключение 
				return HttpResponse('Invalid heder found.')
			post = form.save() # сохраняем введенные данные в бд
			post.save()
			return redirect('success')
	return render(request, 'landing/email.html', {'form': form})

def successView(request):
	return render(request,'landing/thank.html')
