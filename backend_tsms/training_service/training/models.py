from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class Venue(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    institute_id = models.CharField(max_length=100)
    createdBy_id = models.CharField(max_length=100)

    location_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-capacity']

    def __str__(self):
        return self.location_name


class AudienceCategory(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    institute_id = models.CharField(max_length=100)
    createdBy_id = models.CharField(max_length=100)

    category_name = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [ '-created_at']

    def __str__(self):
        return self.category_name


class Training(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    institute_id = models.CharField(max_length=100)
    createdBy_id = models.CharField(max_length=100)
    venue_id = models.ForeignKey(Venue, blank=True,null=True,on_delete=models.DO_NOTHING)

    extra_venue_name = models.CharField(max_length=40,null=True,blank=True)
    trainer = models.CharField(max_length=255,null=True,blank=True)
    # AudienceCategory_id = models.ManyToManyField(AudienceCategory,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    MODE = (
        (0, _('Physical')),
        (1, _('Online')),
        )

    STATUS = (
        (0, _('UpComing')),
        (1, _('OnGoing')),
        (2, _('Cancelled')),
        (3, _('Postponed')),
        )

    mode_of_delivery = models.IntegerField(
    choices=MODE, default=0, verbose_name=_("Mode  of Delivery"))

    description = models.TextField(blank=False,null=False,max_length=30)
    theme = models.CharField(max_length=255,null=False,blank=False)
    cost = models.FloatField(blank=True, null=True)
    topic = models.CharField(max_length=30,blank=False,null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    participant_limit = models.PositiveIntegerField(default=0)

    status = models.IntegerField(default=0,choices=STATUS,verbose_name=_("Status"))

    slots_remaining = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.topic

class AudienceCategoryTraining(models.Model):
    training = models.ForeignKey(Training,blank=True,null=True,on_delete=models.DO_NOTHING)
    audienceCategory = models.ForeignKey(AudienceCategory,blank=True,null=True,on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.training} : {self.AudienceCategory}'

    class Meta:
        unique_together = (("training","audienceCategory"),)

    def __str__(self):
        return self.training.topic


class TrainingApplication(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    institute_id = models.CharField(max_length=100)
    createdBy_id = models.CharField(max_length=100)
    training_id = models.ForeignKey(Training,blank=True, null=True,on_delete=models.SET_NULL)

    train_appller = models.CharField(max_length=255,null=True,blank=True) #save user instance logged in user

    REQUEST = (
        (0, _('Pool')),
        (1, _('Individual')),
        )

    FEEDBACK = (
        (0, _('Pending')),
        (1, _('Approved with changes')),
        (2, _('Approved')),
        (3, _('Rejected'))
        )

    request_type = models.IntegerField(default=0,choices=REQUEST,verbose_name="Request_Type")

    participant_no = models.PositiveIntegerField(default=0)
    status_feedback = models.IntegerField(default=0,choices=FEEDBACK,verbose_name="Feedback Status")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [ '-status_feedback']

    def __str__(self):
        return str(self.status_feedback)




