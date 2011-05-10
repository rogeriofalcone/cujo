from django.conf.urls.defaults import patterns, url

from reminders.forms import ReminderForm_days
 

urlpatterns = patterns('reminders.views',
    url(r'^list/$', 'reminder_list', (), 'reminder_list'),
    url(r'^list/expired/$', 'expired_remider_list', (), 'expired_remider_list'),
    url(r'^add/date/$', 'reminder_add', (), 'reminder_add'),
    url(r'^add/days/$', 'reminder_add', ({'form_class': ReminderForm_days}), 'reminder_add_days'),
    url(r'^edit/(?P<reminder_id>\d+)/date/$', 'reminder_edit', (), 'reminder_edit'),
    url(r'^edit/(?P<reminder_id>\d+)/days/$', 'reminder_edit', ({'form_class': ReminderForm_days}), 'reminder_edit_days'),
    url(r'^(?P<reminder_id>\d+)/$', 'reminder_view', (), 'reminder_view'),
    url(r'^(?P<reminder_id>\d+)/delete/$', 'reminder_delete', (), 'reminder_delete'),
    url(r'^multiple/delete/$', 'reminder_multiple_delete', (), 'reminder_multiple_delete'),
)