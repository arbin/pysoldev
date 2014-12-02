from django.template.response import TemplateResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from django import forms
from captcha.fields import CaptchaField


class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()
    
    
def home(request):
    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            human = True
            subject = 'Message'
            message = request.POST['message']
            sender = 'Pysoldev <arbin@pysoldev.com>'
            recipient = ['arbin@pysoldev.com']

            email = EmailMessage(subject, message, sender, recipient)
            email.send()
        
            messages.success(request, "<h1>You message is on it's way!</h1> <p>No "
                                  "actual tarsiers were harmed in the sending "
                                  "of this message.</p>")
    else:
        form = CaptchaTestForm()
    
    return TemplateResponse(request, 'home.html', locals())


def arbin(request):
    return TemplateResponse(request, 'arbin.html', None)