from django.db import models

# Create your models here.

COMPANY_TYPE = (
    ('IT','IT'),
    ('Non IT','Non IT'),
    ('Mobiles Phones','Mobiles Phones'),
)

#Creating Company Model
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=COMPANY_TYPE)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' --- ' + self.location

#Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl')
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
