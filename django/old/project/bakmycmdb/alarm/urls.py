from django.conf.urls import include, url

urlpatterns = [
    url(r'^alarmAdd/$', 'alarm.views.alarmAdd'),
    url(r'^alarmList/$', 'alarm.views.alarmList'),
    url(r'^alarmEdit/$', 'alarm.views.alarmEdit'),
    url(r'^alarmDel/$', 'alarm.views.alarmDel'),
]