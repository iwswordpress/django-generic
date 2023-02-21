from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    web_id = models.CharField(max_length=50, unique=False, null=True)
    slug = models.SlugField(max_length=255, default="slug")
    name = models.CharField(max_length=255, default="NO-PRODUCT-NAME")
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category)
    is_active = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_id = models.PositiveIntegerField(primary_key=True, db_column="brand_id")
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(max_length=100, default="no-brand")

    def __str__(self):
        return self.name


class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
