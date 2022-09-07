from django.db import models

from .student import Student
from .subject import Subject


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.FloatField(blank=False, null=False)
