from django.db import models

# Create your models here.


class Property(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    room = models.CharField(max_length=255)
    address = models.TextField()
    landmark = models.CharField(max_length=255, blank=True)
    bhk = models.IntegerField()
    bathroom = models.IntegerField()
    area = models.IntegerField()
    price = models.IntegerField()
    furnished = models.CharField(max_length=10)
    image = models.ImageField(upload_to='property_images/', blank=True)

    def __str__(self):
        return "%s %s %s %s %s" %(self.phone, self.room, self.price, self.fullname, self.area)
  

class RentalProperty(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    room = models.CharField(max_length=255)
    address = models.TextField()
    landmark = models.CharField(max_length=255, blank=True)
    bhk = models.IntegerField()
    bathroom = models.IntegerField()
    area = models.IntegerField()
    price = models.IntegerField()
    deposit = models.IntegerField()
    furnished = models.CharField(max_length=11, choices=[('Yes', 'Furnished'), ('Semi', 'Semi Furnished'), ('No', 'Not Furnished')])
    image = models.ImageField(upload_to='rental_property_images/', blank=True)

    def __str__(self):
        return "%s %s %s %s" %(self.fullname, self.room, self.price, self.phone)

