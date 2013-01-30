from django.template.response import TemplateResponse
from django.core.mail import EmailMessage
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        subject = 'Message'
        message = request.POST['message']
        sender = 'Pysoldev <arbin@pysoldev.com>'
        recipient = ['arbin@pysoldev.com']

        email = EmailMessage(subject, message, sender, recipient)
        email.send()
        
        messages.success(request, "<h1>You message is on it's way!</h1> <p>No "
                                  "actual ponies were harmed in the sending "
                                  "of this message.</p>")

    return TemplateResponse(request, 'index.html', None)
