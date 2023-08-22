from django.db import models


class User(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    LANGUAGE_CHOICES = [
        ('nepali', 'Nepali'),
        ('english', 'English'),
        ('other', 'Other'),
    ]
    COUNTRY_CHOICES = [
        ('nepal', 'Nepal'),
        ('india', 'India'),
        ('china', 'China'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)

    def __str__(self):
        return self.name
