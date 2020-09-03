from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class User(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[RegexValidator(
            # 全角カタカナと半角・全角スペースのみ許容
            regex=u'^[ァ-ヶ 　]+$',
            message='全角カタカナのみ有効です',
        )])
    number = models.CharField(max_length=15)

    def is_current_in(self):
        return Attendance.objects.filter(user=self).order_by('-accepted_at').first().is_in

    def __str__(self):
        return self.name

class Attendance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    is_in = models.BooleanField()
    accepted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-accepted_at']

    def __str__(self):
        attendance = '入室' if self.is_in else '退室'
        return f'{self.user} {attendance} {self.accepted_at}'
