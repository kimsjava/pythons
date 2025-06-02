from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField(default=False)  # gender 필드 추가
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def toString(self):
        return f"Name: {self.name}, Mail: {self.mail}, Gender: {'남성' if self.gender else '여성'}, Age: {self.age}, Birthday: {self.birthday}"
    
    def __str__(self):
        return self.toString()
    