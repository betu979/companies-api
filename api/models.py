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

#Employee Model