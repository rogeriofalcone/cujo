from __future__ import absolute_import

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from dynamic_search.api import register

from .literals import PARTICIPANT_ROLE_CHOICES, PREEMPTIVE_CHOICES


class Reminder(models.Model):
    label = models.CharField(max_length=64, verbose_name=_(u'label'))
    notes = models.TextField(blank=True, verbose_name=_(u'notes'))
    datetime_created = models.DateField(blank=True, verbose_name=_(u'creation date'), default=datetime.datetime.now())
    datetime_expire = models.DateField(verbose_name=_(u'expiration date'))

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = _(u'reminder')
        verbose_name_plural = _(u'reminders')

    def __unicode__(self):
        return self.label

    @models.permalink
    def get_absolute_url(self):
        return ('reminder_view', [self.pk])

    def save(self, *args, **kwargs):
        new_instance = not self.pk
        if new_instance:
            if not self.datetime_created:
                self.datetime_created = datetime.datetime.now()

        super(Reminder, self).save(*args, **kwargs)


class Participant(models.Model):
    reminder = models.ForeignKey(Reminder, verbose_name=_(u'reminder'))
    user = models.ForeignKey(User, verbose_name=_(u'user'))
    role = models.CharField(max_length=2, choices=PARTICIPANT_ROLE_CHOICES, verbose_name=_(u'role'))

    class Meta:
        unique_together = ('reminder', 'user', 'role')
        verbose_name = _(u'participant')
        verbose_name_plural = _(u'participants')

    def __unicode__(self):
        return unicode(self.user.get_full_name() if self.user.get_full_name() else self.user)


class Notification(models.Model):
    reminder = models.ForeignKey(Reminder, verbose_name=_(u'reminder'))
    participant = models.ForeignKey(Participant, verbose_name=_(u'participant'))
    preemptive = models.CharField(max_length=4, choices=PREEMPTIVE_CHOICES, verbose_name=_(u'preemptive'))

    class Meta:
        verbose_name = _(u'notification')
        verbose_name_plural = _(u'notifications')

    def __unicode__(self):
        return self.label


register(Reminder, _(u'reminder'), [u'label', 'notes', 'participant__user__username', 'participant__user__first_name', 'participant__user__last_name'])
