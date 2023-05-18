from django.shortcuts import render
from .models import data
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def contact(request):
    mydata = data.objects.first()
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,
            f'{email} has send you the message below: \n{message}',
            email,
            [settings.EMAIL_HOST_USER],
        )
    return render(request, 'contact.html', {'data': mydata})
