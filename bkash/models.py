from django.db import models

# Create your models here.
class Pay_Method(models.Model):
    pay_option = models.CharField(max_length=50)
    min_pay = models.IntegerField()
    max_pay = models.IntegerField(default=1000)

    def __str__(self):
        return self.pay_option
    
    
