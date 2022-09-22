from django.contrib import admin
from .models import PaymentMethod,Payment


# Register your models here.
admin.site.register(PaymentMethod)
admin.site.register(Payment)

