from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# USE GET - ERROR
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        messages.success(request, 'Your request has been submitted, we will get back to you via Email')
        return redirect('index')
    return render(request, 'contacts/contact.html')
