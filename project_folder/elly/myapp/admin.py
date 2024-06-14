from django.contrib import admin

# Register your models here.
# main/admin.py
from .models import Student
from .models import Product
from .models import Teachers

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Teachers)