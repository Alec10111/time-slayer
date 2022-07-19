from django.db import models
from django.conf import settings


class Goal(models.Model):
    title = models.CharField(max_length=20)  # eg. 'Meditate', 'Workout'
    description = models.TextField(max_length=100)
    frequency = models.CharField(max_length=20)  # eg. 'Daily', 'Weekly'
    amount = models.CharField(max_length=20)  # eg. '3h', '2h30m' '5t'(times)
    created = models.DateTimeField()  # Timestamp
    recurring = models.BooleanField()  # True/False


class History(models.Model):
    goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    started_date = models.DateTimeField()  # Timestamp
    end_date = models.DateTimeField()  # Timestamp
    amt_done = models.CharField(max_length=20)  # eg. '15m' '1' '1h2m13s'


class Current_Goal(models.Model):
    goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amd_recorded = models.CharField(max_length=20)  # eg. '15m' '1' '1h2m13s'
