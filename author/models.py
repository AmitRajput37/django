from django.db import models

# Create your models here.


class Author(models.Model):
    aname = models.CharField("author_name",max_length=50)
    aage = models.IntegerField("author_age")
    aexp = models.CharField("author_exp", max_length=50)
    aemail = models.EmailField("author_email",max_length=50)

    class Meta:
        db_table = 'Author_Info'


class Address(models.Model):
    city = models.CharField("City",max_length=50)
    pincode = models.IntegerField("Pin_code")
    state = models.CharField("State",max_length=50)
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Address_Info'