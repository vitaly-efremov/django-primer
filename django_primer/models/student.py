from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)

    @property
    def fio(self):
        if self.name and self.surname:
            return f'{self.name} {self.surname}'
        return self.name or self.surname

    def __repr__(self):
        return f'Student(name="{self.name}", surname="{self.surname}", email="{self.email}")'
