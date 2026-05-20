from django.contrib import admin

# Register your models here.
from .models import Pay_Method

class pay_methodAdmin(admin.ModelAdmin):
    list_display = ('id', 'pay_option', 'min_pay', 'max_pay')
admin.site.register(Pay_Method, pay_methodAdmin)
