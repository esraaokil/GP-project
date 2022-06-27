from django.db import models
from PIL import Image
import os
import uuid
from django.core.validators import RegexValidator


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class Profile(models.Model):
    type_choices= (
        ('doctor','doctor'),
        ('patient','patient')
    )

    six=(
        ('male','male'),
        ('famale','famale')
    )
    type_name=models.CharField(max_length=50, blank=True,null=True,  choices=type_choices)
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=500, blank=True,null=True )
    password = models.CharField(max_length=200, blank=True,null=True)
    gander= models.CharField(max_length=50, blank=True,null=True, choices=six)
    #city = models.CharField(max_length=200, blank=True, )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,  blank=True,null=True, unique=True) # Validators should be a list
    #created = models.DateTimeField(default=datetime(2017, 7, 28, 7, 58, 21))
    profile_image=models.ImageField(upload_to=upload_to, blank=True, null=True)
    #type_id=models.OneToOneField(Type, related_name='type_profile', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=['name']   
    

    