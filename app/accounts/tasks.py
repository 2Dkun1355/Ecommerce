import time

from celery import shared_task

from accounts.models import CustomUser



@shared_task(name='Admin send mails')
def send_daily_message():
    admins = CustomUser.objects.filter(is_superuser=True)
    for admin in admins:
        admin.first_name = 'TEST'
        admin.save()


@shared_task(name='Test')
def test(word):
    print(word)
    return f'Result: {word}'



