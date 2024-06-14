from django.db import models

# Create your models here.
# main/models.py

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_name}"
    
class Teachers(models.Model):
    teacher_name=models.CharField(max_length=100)
    teacher_gender=models.Choices
    teacher_email=models.EmailField
    def __str__(self):
        return f"{self.teacher_name}"

