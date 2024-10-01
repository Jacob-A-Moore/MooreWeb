from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = f'Contact Form Submission from {name}'
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f'Email: {email}\nMessage: {message}'

            send_mail(
                subject,
                full_message,
                email,
                ['jakedawg99@gmail.com'],
            )
            ##handle form submission
            messages.success(request, 'Thank you! Your message was sent and I will get back to you as soon as possible')
            return redirect('home')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form':form})
            
