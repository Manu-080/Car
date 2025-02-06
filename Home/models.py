from django.db import models


# Create your models here.
class Transmission(models.Model):
    gearbox = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.gearbox

class BodyType(models.Model):
    body_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.body_type
    
    class Meta:
        ordering = ['body_type']
    

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None,null=True)
    
    def __str__(self) -> str:
        return self.name
    
class Car(models.Model):
    fuel_type = (
        ('petrol','petrol'),
        ('diesel','diesel'),
        ('hybrid','hybrid'),
    )
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100,default=name)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='car_brand')
    priority = models.IntegerField(default=0)
    price = models.CharField(max_length=50)
    horsepower = models.CharField(max_length=10)
    torque = models.CharField(max_length=50)
    fuel = models.CharField(choices=fuel_type,max_length=50)
    body = models.ForeignKey("BodyType",on_delete=models.CASCADE,related_name='body_style',null=True)
    transmission = models.ForeignKey("Transmission", on_delete=models.CASCADE,related_name='gearbox_type',null=True)


    def __str__(self) -> str:
        return self.name
    