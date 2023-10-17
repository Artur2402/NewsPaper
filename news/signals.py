# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from django.dispatch import receiver
#
# from .models import Post
#
# @receiver(post_save, sender=Post)
# def post_created(instance, created, **kwargs):
#     if not created:
#         return
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.post_category
#     ).values_list('email', flat=True)
#
#     subject = f'Новый пост в категории {instance.post_category}'
#
#     text_content = (
#         f'{instance.heading}\n'
#         f'{instance.text.preview()}\n\n'
#         f'Читать статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#
#     html_content = (
#         f'{instance.heading}<br>'
#         f'{instance.text.preview()}<br><br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Читать пост</a>'
#     )
#
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()


from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post, Subscription

from .send_email import send_email


@receiver(post_save, sender=Post)
def create_post(sender, instance, created, **kwargs):
    if created:
        category_list = instance.post_category.all()

        for category in category_list:
            subscriber_list = Subscription.objects.filter(
                category=category
            )

            for s in subscriber_list:
                text_base = '''
					Вышел новый пост <br>
					<a href="http://127.0.0.1:8000/news/{post_id}/">Читать пост</a>
				'''
                text_html = text_base.replace('{post_id}', str(instance.id))
                to_email = s.user.email
                send_email(message=text_html, recipient_list=to_email)


@receiver(post_save, sender=Post)
def save_post(sender, instance, **kwargs):
    category_list = instance.post_category.all()

    for category in category_list:
        subscriber_list = Subscription.objects.filter(
            category=category
        )

        for s in subscriber_list:
            text_base = '''
				Вышел новый пост <br>
				<a href="http://127.0.0.1:8000/news/{post_id}/">Читать пост</a>
			'''
            text_html = text_base.replace('{post_id}', str(instance.id))
            to_email = s.user.email
            send_email(message=text_html, recipient_list=to_email)