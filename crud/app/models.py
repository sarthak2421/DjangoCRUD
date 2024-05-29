from django.db import models

# Create your models here.


class Orders(models.Model):
    oid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    price = models.IntegerField()
    email = models.CharField(max_length=70)
    addr = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.fname + self.lname