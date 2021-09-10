from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string

from proj.settings import EMAIL_HOST_USER


def send_review_email(name, email_address, review):
    context = {
        'name': name,
        'email': email_address,
        'review': review
    }
    
    email_subject = "Thank you for your review"
    email_body = render_to_string('task2/email_message.txt', context)

    email = EmailMessage(
        email_subject,
        email_body,
        EMAIL_HOST_USER,
        [email_address, ]
    )

    return email.send(fail_silently=False)