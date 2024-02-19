from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date
# Create your models here.
class House_data(models.Model):
    house_name = models.CharField(max_length=20)
    house_address = models.CharField(max_length=100)
    house_owner = models.CharField(max_length=100)
    house_owner_phone = models.CharField(max_length=100)
    house_code=models.IntegerField(default=0,unique=True)

    def __str__(self):
        return self.house_name
class Tenant_data(models.Model):
    Name=models.CharField(max_length=50,unique=True)
    House_Name=models.ForeignKey(House_data,on_delete=models.CASCADE)
    D_O_B=models.DateField(blank=False)
    Address=models.CharField(max_length=100,blank=True)
    Email=models.EmailField(unique=True,blank=True,null=True)
    Phone_No=models.CharField(max_length=10,blank=False,null=True)
    Meater_Reading=models.CharField(max_length=100,blank=True)
    Room_No=models.IntegerField( blank=False)
    Tenant_image=models.ImageField(upload_to='photos/',blank=True)
    Work_Place=models.CharField(max_length=100,blank=True)
    Members=models.IntegerField()
    Members_Name=models.CharField(max_length=100,blank=True)
    Rent=models.CharField(max_length=5)
    Advance=models.CharField(max_length=5)
    Arrived_Month=models.DateField()
    Bill_unit=models.IntegerField()
    Documents_Upload=RichTextUploadingField(blank=True)
    Balance=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.Name
class Payments_data(models.Model):
    Tenant_Name=models.ForeignKey(Tenant_data,on_delete=models.CASCADE)
    House_Name=models.ForeignKey(House_data,on_delete=models.CASCADE)
    Rent_Amount=models.IntegerField()
    Date=models.DateField()
    Payment_date=models.DateField(blank=True,null=True)
    Mode=models.CharField(max_length=20)
    Payment_Screenshot=models.ImageField(upload_to='payments/',blank=True)
    Previous_Electricity_Unit=models.IntegerField()
    Current_Electricity_Unit=models.IntegerField()
    Total_Bill=models.IntegerField()
    Unit_Price=models.IntegerField()
    Water_Bill=models.IntegerField()
    Total_Amount=models.IntegerField()
    def __str__(self):
        return str(self.Tenant_Name)
class Old_record(models.Model):
    Tenant_Name=models.CharField(max_length=50)
    Room_No=models.IntegerField(blank=False,null=True)
    House_Name=models.CharField(max_length=50)
    D_O_B=models.DateField()
    Address=models.CharField(blank=True,max_length=200)
    Email=models.EmailField(blank=True,null=True)
    Date=models.DateField()
    Checkin_Date=models.DateField()
    Phone_No=models.CharField(max_length=10)
    Tenant_image=models.ImageField(upload_to='old_photo/',blank=True)
    Rent=models.CharField(max_length=10)
    Documents_Upload=RichTextUploadingField(blank=True)
    def __str__(self):
        return (self.Tenant_Name)
class Old_payment(models.Model):
    Tenant_Name=models.ForeignKey(Old_record, on_delete=models.CASCADE,null=True)
    House_Name=models.CharField(max_length=50, blank=False, null=True)
    Rent_Amount=models.IntegerField()
    Date=models.DateField()
    Mode=models.CharField(max_length=20)
    Payment_Screenshot=models.ImageField(upload_to='payments/',blank=True)
    Previous_Electricity_Unit=models.IntegerField()
    Current_Electricity_Unit=models.IntegerField()
    Total_Bill=models.IntegerField()
    Unit_Price=models.IntegerField()
    Water_Bill=models.IntegerField()
    Total_Amount=models.IntegerField()
    def __str__(self):
        return str(self.Tenant_Name)        
    
