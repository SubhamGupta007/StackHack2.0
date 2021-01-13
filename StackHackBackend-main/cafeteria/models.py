from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.core.validators import MinLengthValidator, EmailValidator, MaxLengthValidator, URLValidator

def content_file_name(instance,filename):
	ext="png"
	filename= str(instance.user.username)+"."+str(ext)
	return os.path.join('images/food/',filename)

class Food(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    food_code = models.CharField(null=True,max_length=20)
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    price = models.IntegerField(null=True)
    image_url = models.URLField(null=True)
    image = models.ImageField(null=True, upload_to=content_file_name)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.food_code + " " + self.name

    def save(self,  *args, **kwargs):
        if self.image:
          img= Image.open(self.image)
          output = BytesIO()
          img = img.resize((100, 100))
          img.save(output, format='PNG', quality=100)
          output.seek(0)
          self.image = InMemoryUploadedFile(output, 'ImageField', ".png" , 'image/png',
                                        sys.getsizeof(output), None)
        super(Profile, self).save()

    class Meta:
        managed = True