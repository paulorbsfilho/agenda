from django.db import models

# Create your models here.

class Contact(models.Model):
    class Meta:
        db_table = 'Contact'
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cell = models.CharField(max_length=15)
    email = models.CharField(max_length=80)

    def __str__(self):
        return self.first_name