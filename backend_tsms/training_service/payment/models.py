from django.db import models
from training.models import Training
import uuid

# Create your models here.
class PaymentMethod(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    institute_id = models.CharField(max_length=100)
    createdBy_id = models.CharField(max_length=100)

    payment_method = models.CharField(max_length=20,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-payment_method']

    def __str__(self):
        return self.payment_method

class Payment(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    institute_id = models.CharField(max_length=100)
    createdBy_id = models.CharField(max_length=100)
    training_id = models.ForeignKey(Training, blank=True,null=True, on_delete=models.SET_NULL)
    payment_method_id = models.ForeignKey(PaymentMethod, blank=True,null=True, on_delete=models.CASCADE)

    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-created_at']

    def __str__(self):
        return str(self.amount)


