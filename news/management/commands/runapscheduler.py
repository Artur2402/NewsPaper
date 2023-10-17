import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

logger = logging.getLogger(__name__)

from ...models import Post, Subscription, PostCategory
from ...send_email import send_email
from django.utils import timezone
from datetime import datetime, timedelta


def my_job():
    category_list = PostCategory.objects.all()
    now = timezone.now()
    for category in category_list:
        subscription_list = Subscription.objects.filter(
            category=category
        )

        # посты ids_list = [1, 3, 5, ...]
        # post_list = Post.objects.filter(
        #         postCategory__ids=[category.id],
        #         # дата создания с (>=) пятницы 18:00
        #         create_post__gte=now-timedelta(days=7),
        #     ).values_list(
        #         'id', flat=True
        #     ).order_by(
        #         'id'
        #     )
        post_list = Post.objects.filter(
            post_сategory__id__in=[category.category.id],
            # дата создания с (>=) пятницы 18:00
            create_post__gte=now - timedelta(days=7),
        )

        text_html = 'Новые посты на сайте <br>'

        text_base = '''
            <a href="http://127.0.0.1:8000/news/{post_id}/">{heading} - Читать пост</a>
            <br>
        '''

        for post in post_list:
            str_title = text_base.replace('{heading}', str(post.heading))
            text_html += str_title.replace('{post_id}', str(post.id))

        for s in subscription_list:
            to_email = s.user.email
            send_email(text_html, to_email)
    pass


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="fri", hour="18", minute="00"
            ),  # В пятницу 18:00, через каждую неделю.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")