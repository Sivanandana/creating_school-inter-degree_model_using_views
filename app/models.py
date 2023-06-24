from django.db import models

# Create your models here.
class School(models.Model):
    school_name=models.CharField(max_length=70,primary_key=True)
    def __str__(self) -> str:
        return self.school_name

class Inter(models.Model):
    school_name=models.ForeignKey(School,max_length=70,on_delete=models.CASCADE)
    collage_name=models.CharField(max_length=50,primary_key=True)

    def __str__(self) -> str:
        return self.collage_name

class Degree(models.Model):

    collage_name=models.ForeignKey(Inter,max_length=90,on_delete=models.CASCADE)
    group=models.CharField(max_length=80) 