from django.db import models

# Create your models here.

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100 )  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    eage=models.IntegerField( null=True)
    eaddress=models.CharField(max_length=100, null=True) 
    eLK=models.CharField(max_length=100, null=True) 
    eimage=models.ImageField(upload_to='media',default="/media/default.png")
    class Meta:  
        db_table = "employee"  
