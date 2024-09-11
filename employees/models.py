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

    # Employee's address
    address = models.CharField(max_length=255)

    # Employee's email
    email = models.EmailField()

    # Educational background
    education_background = models.CharField(max_length=255)

    # Contact number
    contact = models.CharField(max_length=15)

    # Date of birth (day, month, year)
    dob = models.DateField()

    # National Identification Number (NIN)
    nin = models.CharField(max_length=14)

    def __str__(self):
        return self.name

