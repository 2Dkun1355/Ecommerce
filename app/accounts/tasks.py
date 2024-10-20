from celery import shared_task

from accounts.models import CustomUser



@shared_task(name='Admin send mails')
def send_daily_message():
    admins = CustomUser.objects.filter(is_admin=True)
    for admin in admins:
        admin.first_name = 'TEST'
        admin.save()


@shared_task(name='Test')
def test():
    print(' ***** TEST ***** ')