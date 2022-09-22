from django.db import models
from training.models import Training
import uuid

# Create your models here.
class TrainingAttendance(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    institute_id = models.CharField(max_length=100)
    createdBy_id = models.CharField(max_length=100)
    training_id = models.ForeignKey(Training, blank=True,null=True,on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)
