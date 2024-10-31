from django.db import models

class Employee(models.Model):
    # Employee's full name
    name = models.CharField(max_length=100)

    # Gender choices
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    
    address = models.CharField(max_length=255)

    email = models.EmailField()

    education_background = models.CharField(max_length=255)

    contact = models.CharField(max_length=15)

    dob = models.DateField()

    nin = models.CharField(max_length=14)

    def __str__(self):
        return self.name

