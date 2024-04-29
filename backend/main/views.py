from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'New Contact Message'
            message = f'Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}'
            sender = form.cleaned_data['email']
            recipient = ['samuelbendavid01@gmail.com']

            send_mail(subject, message, sender, recipient, fail_silently=False)
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'backend/index.html', {'form': form}
    )
