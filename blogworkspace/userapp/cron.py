# import logging
# from django_cron import CronJobBase, Schedule
# from django.core.mail import send_mail
# from django.utils.timezone import now
# from django.contrib.auth.models import User
# import datetime

# # Enable logging
# logger = logging.getLogger(__name__)

# class SendEmailAfterLogin(CronJobBase):
#     RUN_EVERY_MINS = 1  # Runs every 1 minute
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'userapp.send_email_after_login'  # Use your correct app name

#     def do(self):
#         one_minute_ago = now() - datetime.timedelta(minutes=1)
#         users = User.objects.filter(last_login__gte=one_minute_ago)

#         logger.info(f"Checking for users logged in since: {one_minute_ago}")
#         logger.info(f"Users found: {[user.email for user in users]}")

#         for user in users:
#             if user.email:  # Check if user has an email
#                 try:
#                     send_mail(
#                         'You Are Still Logged In!',
#                         f'Hello {user.username}, you have been logged in for 1 minute!',
#                         'your_email@gmail.com',
#                         [user.email],
#                         fail_silently=False,
#                     )
#                     logger.info(f"Email sent successfully to {user.email}")
#                 except Exception as e:
#                     logger.error(f"Failed to send email to {user.email}: {e}")
#             else:
#                 logger.warning(f"User {user.username} has no email, skipping...")
