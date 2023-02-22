# Insert into single table with one-to-one relationship

```python
from inventory.models import Product, ProductInventory, Brand, ProductType, Stock

Product.objects.create(web_id='123',slug='ex1',name='ex1',description='ex1',is_active=True)
Brand.objects.create(brand_id=1,name='ex1')
ProductType.objects.create(name="shoe")
ProductInventory.objects.create(sku='123',upc='123',product_type_id=1,product_id=1,brand_id=1, retail_price='10.00', store_price='10.00', sale_price='10.00', weight='100')

Stock.objects.create(product_inventory_id=1,units=100)

```
