from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number
