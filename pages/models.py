from email.policy import default
from django.db import models
from django.utils import timezone
# from datetime import datetime
# from ckeditor.fields import RichTextField
# from multiselectfield import MultiSelectField 

# full NAME
# type of services
# Phone  number
# date of appointment
# Message
# building names
# Flat number


    
class Plumbing(models.Model):

        full_name = models.CharField(max_length=255)
        phone = models.CharField(max_length=255)
        flat_no = models.CharField(max_length=255)
        building_names = models.CharField(max_length=255)
        type_of_services = models.CharField(max_length=255)
        date = models.DateTimeField()
        message = models.TextField()
        purpose = models.CharField(max_length=255, blank=True)
        
        def __str__(self):
                return self.full_name

class Painting(models.Model):

        full_name = models.CharField(max_length=255)
        phone = models.CharField(max_length=255)
        flat_no = models.CharField(max_length=255)
        building_names = models.CharField(max_length=255)
        type_of_services = models.CharField(max_length=255)
        date = models.DateTimeField()
        message = models.TextField()
        purpose = models.CharField(max_length=255, blank=True)
        
        def __str__(self):
                return self.full_name
        
class Tilesfix(models.Model):

        full_name = models.CharField(max_length=255)
        phone = models.CharField(max_length=255)
        flat_no = models.CharField(max_length=255)
        building_names = models.CharField(max_length=255)
        type_of_services = models.CharField(max_length=255)
        date = models.DateTimeField()
        message = models.TextField()
        purpose = models.CharField(max_length=255, blank=True)
        
        def __str__(self):
                return self.full_name


class Electrical(models.Model):

        full_name = models.CharField(max_length=255)
        phone = models.CharField(max_length=255)
        flat_no = models.CharField(max_length=255)
        building_names = models.CharField(max_length=255)
        type_of_services = models.CharField(max_length=255)
        date = models.DateTimeField()
        message = models.TextField()
        purpose = models.CharField(max_length=255, blank=True)
        
        def __str__(self):
                return self.full_name
        
class Furniture(models.Model):

        full_name = models.CharField(max_length=255)
        phone = models.CharField(max_length=255)
        flat_no = models.CharField(max_length=255)
        building_names = models.CharField(max_length=255)
        type_of_services = models.CharField(max_length=255)
        date = models.DateTimeField()
        message = models.TextField()
        purpose = models.CharField(max_length=255, blank=True)
        
        def __str__(self):
                return self.full_name
        
class Accodition(models.Model):

        full_name = models.CharField(max_length=255)
        phone = models.CharField(max_length=255)
        flat_no = models.CharField(max_length=255)
        building_names = models.CharField(max_length=255)
        type_of_services = models.CharField(max_length=255)
        date = models.DateTimeField()
        message = models.TextField()
        purpose = models.CharField(max_length=255, blank=True)
        
        def __str__(self):
                return self.full_name
# Create your models here.
