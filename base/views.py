from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

def Main(request):
    return render(request, 'home.html')

def Contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send email
        # send_mail
        #     'message_name', # subject
        #     message, # message
        #     message_email, # from email
        #     ['manuelhayashi@icloud.com'], # to email
        #     )
        context = {'message_name': message_name}
        return render(request, 'home.html', context)
    else:
        return render(request, 'contact_form.html', {})
