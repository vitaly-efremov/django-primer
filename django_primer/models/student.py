from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)

    @property
    def fio(self):
        return f'{self.name} {self.surname}'
