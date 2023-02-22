# Insert data into multiples tables & using atomic operations

In one statement: No
In one transaction: Yes

```python
from inventory.models import Product, ProductInventory, Brand, ProductType, Stock

Product.objects.all().delete()
Brand.objects.all().delete()
ProductType.objects.all().delete()
ProductInventory.objects.all().delete()

Product.objects.create(web_id='123',slug='ex1',name='ex1',description='ex10000',is_active=True)

Brand.objects.create(brand_id=1,name='ex1')

ProductType.objects.create(name="shoe")

ProductInventory.objects.create(sku='123',upc='123',product_type_id=1,product_id=2,brand_id=1, retail_price='10.00', store_price='10.00', sale_price='10.00', weight='100')

Stock.objects.create(product_inventory_id=1,units=100)

```

```python

# url.py
from inventory import views
path('test/', views.example)

# view example
def example(request):

from django.http import HttpResponse
from inventory.models import ProductInventory, Stock
from django.db import IntegrityError, transaction


def new(request):

    try:
        with transaction.atomic():
            ProductInventory.objects.create(sku='1234',upc='1234',product_type_id=3,product_id=11,brand_id=1, retail_price='10.00', store_price='10.00', sale_price='10.00', weight='100')

            Stock.objects.create(product_inventory_id=6,units=100)
    except IntegrityError:
        return HttpResponse("Error")

    return HttpResponse("Hi")
```
