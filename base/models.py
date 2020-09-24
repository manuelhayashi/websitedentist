# from django.db import models

# Create your models here.
# class CustomerMessage(models.Model):
#     fname = models.CharField(max_length=200, null=True)
#     lname = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=10, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#
#     def __str__(self):
#         return self.name


# class CustomerMessage(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     message = models.CharField(max_length=1500, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     # customer = models.ForeignKey(Customer)
#
#     def __str__(self):
#         return self.name
