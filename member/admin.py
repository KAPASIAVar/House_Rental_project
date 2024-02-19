from django.contrib import admin
from .models import House_data,Tenant_data,Payments_data,Old_record,Old_payment
# Register your models here.
admin.site.register(House_data)
admin.site.register(Tenant_data)
admin.site.register(Payments_data)
admin.site.register(Old_record)
admin.site.register(Old_payment)
