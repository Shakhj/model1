from django.db import models

# Create your models here. 
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=40)
    ephone_no=models.IntegerField()
    esal=models.FloatField()
    eplace=models.CharField(max_length=50)
    ejob=models.CharField(max_length=40)

    def _str_(self):
    	return(self.ename)