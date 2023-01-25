from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class Login(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)

class work(models.Model):
    name = models.CharField(max_length=100)
    charge = models.IntegerField()

    def __str__(self):
        return self.name

class register(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_pic= models.FileField(upload_to='profilepic/')
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    email = models.EmailField()
    work_type = models.ForeignKey(work,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
class register1(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    email = models.EmailField()

    def __str__(self):
        return self.name

class complaints(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True,blank=True)



class Schedule_add(models.Model):
    worker = models.ForeignKey(register,on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Take_appointment(models.Model):
    user = models.ForeignKey(register1,on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule_add,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


class Bill(models.Model):
    name = models.ForeignKey(register1,on_delete=models.CASCADE)
    bill_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    paid_on = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)


class CreditCard(models.Model):
        card_no = models.CharField(max_length=30)
        card_cvv = models.CharField(max_length=30)
        expiry_date = models.CharField(max_length=200)

