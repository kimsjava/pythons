from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def toString(self):
        return f"Name: {self.name}, Mail: {self.mail}, Age: {self.age}, Birthday: {self.birthday}"
    
    def __str__(self):
        return self.toString()
    