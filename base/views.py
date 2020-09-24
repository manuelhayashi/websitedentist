from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

def Main(request):
    return render(request, 'home.html')

def Contact(request):
    if request.method == "POST":
        message_fname = request.POST['message-fname']
        message_lname = request.POST['message-lname']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send email
        # send_mail(
        #     message_name, # subject
        #     message, # message
        #     message_email, # from email
        #     ['manuel.hayashi@icloud.com'], # to email
        #     )
        context = {'message_fname': message_fname}
        return render(request, 'contact_form.html', context)
    else:
        return render(request, 'contact_form.html', {})
