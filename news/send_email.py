from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import Subscription


def send_email(text_html, to_email):
    subject = 'Почтовая рассылка (вы подписались)'

    # от кого (см. выше settings.py)
    from_email = settings.EMAIL_HOST_USER

    # кому отправить (email)
    to_email = to_email

    # просто текст
    text_content = text_html

    # текст, можно использовать HTML
    html_content = text_html
    # отправка письма
    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        [to_email]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_mass_email(text_html, to_email):
    subject = 'Почтовая рассылка (вы подписались)'

    # от кого (см. выше settings.py)
    from_email = settings.EMAIL_HOST_USER

    # кому отправить (email)
    to_email = to_email
    # to_email = []

    # просто текст
    text_content = text_html

    # текст, можно использовать HTML
    html_content = text_html
    # отправка письма
    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        to_email
        )
    msg.attach_alternative(html_content, "text/html")
    msg.send()