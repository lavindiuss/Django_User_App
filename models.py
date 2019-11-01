from django.db import models
from unique_upload import unique_upload
from django.contrib.auth.models import User



""" for bucket file uploading """ 
def file_upload(instance, filename):
    return unique_upload(instance, filename)



 """ app-user inherit from django user model 
     which have the main common fields like
     first_name,last_name,email,password
     then we can cusomize the others as we want 
 """
class AppUser(User):
    profile_picture = models.ImageField(upload_to=file_upload, blank=True, null=True)
    clup_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)



