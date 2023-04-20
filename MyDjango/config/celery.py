# import os
# import logging
#
# from celery import Celery
# from celery.schedules import crontab
#
# from django.conf import settings
#
# os.environ['DJANGO_SETTINGS_MODULE']='config.settings'
# # os.environ.setdefault('DJANGO_SETTING_MODULE','config.settings')
#
# PRIORITY_HIGH = 0
# PRIORITY_NORMAL = 1
# PRIORITY_LOW = 2
#
# LOCALLY_BLOCKING = False
#
#
# class CeleryConfig:
#     broker_url = settings.REDIS_LOCATION
#     result_backend = settings.REDIS_LOCATION
#     timezone = settings.TIME_ZONE
#     task_ignore_result = True
#     task_remote_traceback = True
#     worker_max_task_per_child = 300
#     worker_lost_waite = 120
#     task_soft_time_limit = 60*4
#     task_time_limit = 60*4*4
#     beat_schedule = None
#     task_default_queue = 'default'
#     broker_transport_options ={
#         'priority_steps':list(range(10)),
#         'visibility_timeout':60*60*24,
#     }
#     task_publish_retry = True
#     task_publish_retry_policy = {
#         'max_retries':2,
#         'interval_start':0.2,
#         'interval_step':0.9,
#         'interval_max':2,
#     }
#
#     task_always_eager = LOCALLY_BLOCKING
#     task_eager_propagates = LOCALLY_BLOCKING
#
#
# CeleryConfig.beat_schedule = {
#     'show_test_task': {
#         'task' : 'mainapp.tasks.message_user2',
#         'schedule' : crontab(minute = 1),
#         'options' : {
#             'priority' : PRIORITY_HIGH,
#         },
#     },
# }
#
# app = Celery('config')
# # app.config_from_object('django.conf.settings',namespace='CELERY')
# app.config_from_object(CeleryConfig)
# app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
#
#
# class ErrorLoggingTask(app.Task):
#     def on_failure(self,exc,task_id,args,kwargs,e_info):
#         message = (
#             f'Celery task exception.'
#             f': {self.name}({task_id})'
#             f'Exception:{exc.__class__.__name__}.'
#
#         )
#
#         if args:
#             message = f'(message) Args: {",".join((str(a) for a in args))}'
#
#         if kwargs:
#             t_kwargs = ','.join(f'{k}:{v}' for k,v in kwargs.items())
#             message = f'{message} Kwargs:{t_kwargs}'
#
#         message = f'{message}.Info:{e_info}'
#         logging.error(message,exc_info=exc)
#          # Logger.error(message,exc_info=exc)


import os
from celery import Celery
from celery.schedules import crontab



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Выполняется каждый понедельник в 08:30 утра.
    'add-every-monday-morning': {
        'task': 'mainapp.tasks.message_me',
        'schedule':crontab(hour=17, minute=30),
    },
}
app.conf.timezone = 'Europe/Minsk'
