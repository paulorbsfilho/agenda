from django.db import models

# Create your models here.

class Contact(models.Model):
    class Meta:
        db_table = 'Contact'
    # photo = models.ImageField(upload_to='media/', null=True, blank=True,
    #                           height_field='height', width_field='width', max_length=200)
    height = 300
    width = 300
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cell = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Contact, related_name="membership")

    def __str__(self):
        return self.name