from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from .models import Project, Skill


def index(request):
    projects = Project.objects.all()
    tools = {}
    for project in projects:
        tools[project] = project.tool.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'New Contact Message'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nMessage: {form.cleaned_data["message"]}'
            sender = form.cleaned_data['email']
            recipient = [settings.EMAIL_HOST_USER]

            send_mail(subject, message, sender, recipient, fail_silently=False)
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'backend/index.html', {'form': form, 'projects': projects, 'tools': tools, 'skills': skills})
