from celery import shared_task

from .send_email import send_mass_email

@shared_task
def send_email_task(text_html, to_email):
    return send_mass_email(text_html, to_email)