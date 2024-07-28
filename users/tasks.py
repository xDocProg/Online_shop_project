from celery import shared_task
from django.core.mail import send_mail
from shop_project import settings


@shared_task
def send_confirmation_email(email, code):
    subject = 'Подтверждение регистрации'
    message = f'Ваш код подтверждения: {code}'
    from_email = settings.EMAIL_HOST
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
