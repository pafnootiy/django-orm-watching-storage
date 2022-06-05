from django.db import models
from django.utils.timezone import localtime
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        entered_time = self.entered_at
        leaved_time = self.leaved_at
        time_duration = 0
        if leaved_time is None:
            time_duration = localtime() - entered_time
        else:
            time_duration = leaved_time - entered_time

        return time_duration.total_seconds()

    def format_duration(self, duration):
        self.duration = duration
        hours = round(duration // 3600)
        minutes = round((duration % 3600) // 60)
        return f" {hours}ч {minutes}м"

    def is_visit_long(self, minutes, duration):
        all_cards = Passcard.objects.all()
        convert_time_for_check = round((duration % 3600) // 60)
        time_for_check = datetime.time(0, convert_time_for_check)
        control_time = datetime.time(0, minutes)
        return not time_for_check < control_time
