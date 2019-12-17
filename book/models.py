from django.db import models
from author.models import Author


class Book(models.Model):
    bname = models.CharField("book_name",max_length=50)
    bprice = models.FloatField("book_price")
    bauthor = models.CharField("book_author", max_length=50)
    bremarks = models.TextField("book_remarks", max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    class Meta:
        db_table='Book_Info'


class Seller(models.Model):
    sname = models.CharField("seller_name",max_length=50)
    city = models.CharField("seller_city",max_length=50)
    address = models.CharField("seller_address",max_length=100)
    book = models.ManyToManyField(Book)

    class Meta:
        db_table = 'Seller_Info'