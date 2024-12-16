from django.db import models

# Create your models here.

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255,unique=True,null=False)
    email=models.CharField(max_length=255,unique=True,null=False)
    password=models.CharField(max_length=255,null=False)
    is_staff=models.BooleanField(default=False)
    a=models
    
    
class Books(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255,null=False)
    author=models.CharField(max_length=255,null=False)
    isbn=models.CharField(max_length=255,unique=True,null=False)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=False)
    publish_date=models.DateTimeField(auto_now_add=True)
    
    
class Orders(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50)
    
    
class OrdersDetails(models.Model):
    id=models.AutoField(primary_key=True)
    
    order_id=models.ForeignKey(Orders, on_delete=models.CASCADE)
    book_id=models.ForeignKey(Books, on_delete=models.CASCADE)

    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=False)
    
    
    


