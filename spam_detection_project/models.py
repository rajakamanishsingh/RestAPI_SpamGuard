from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=128) 
    is_spam = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    is_spam = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} - {self.phone_number}"

class RandomNumber(models.Model):
    phone_number=models.CharField(max_length=20,unique=False)
    is_spam=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.phone_number}"
    
