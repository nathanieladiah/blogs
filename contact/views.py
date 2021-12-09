from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
	if request.method == 'POST':
		# Maybe use the user to fill in some contact info?
		# No because visitors may not be logged in
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']

		contact = Contact(name=name, email=email, phone=phone, message=message)
		
		email_subject = f'New contact {name}: {email} ({phone})'
		send_mail(email_subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

		# Only save the contact if the message sends successfully.
		contact.save() 
		return render(request, 'contact/success.html')
