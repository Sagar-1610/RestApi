from django.db import models

# Create your models here.

class Invoice(models.Model):
    Invoice_no =  models.IntegerField(primary_key=True)
    Date =models.DateField()
    Customer_Name= models.CharField(max_length=60)


class InvoiceDetail(models.Model):
    Invoice_no = models.ForeignKey( Invoice, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=100)

