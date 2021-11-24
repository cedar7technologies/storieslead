from django.db import models

# Create your models here.
class user(models.Model):
    user_id=models.IntegerField(primary_key=True,unique=True)
    nick_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8,blank=False)
    is_active=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True,blank=True)
    class Meta:
        db_table="stories_user"
class presents(models.Model):
    user_id=models.ForeignKey(user,related_name="presents",on_delete=models.CASCADE)
    stories=models.IntegerField(blank=True)
    poems=models.IntegerField(blank=True)
    novels=models.IntegerField(blank=True)
    class Meta:
        db_table="presents"




