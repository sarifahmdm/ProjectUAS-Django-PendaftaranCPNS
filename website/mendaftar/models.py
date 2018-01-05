from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    organizer = models.CharField(max_length=30)
    finished = models.BooleanField()
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['date_begin']

class Visitor(models.Model):
    no_ktp = models.CharField(max_length=18)
    nik = models.CharField(max_length=18)
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    target_event = models.ForeignKey(Event)
    date_join = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.no_ktp

    class Meta:
            ordering = ['date_join']
