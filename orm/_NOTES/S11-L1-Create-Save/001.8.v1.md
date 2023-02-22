# Insert into single table with many-to-many relationship table

```python
from inventory.models import Product, Category, ProductInventory, Brand, ProductType
from django.db import connection, reset_queries

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Category.objects.all().delete()

x = Product(web_id='123456780',slug='ex100000',name='ex100000',description='ex10000',is_active=True)
x.save()
y = Category(name='Flip-Flops', slug='flipflops', is_active=True)
y.save()
x.category.add(y)

cursor = connection.cursor()
cursor.execute("INSERT INTO inventory_product (web_id,slug,name,description,is_active,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s)", ['123456','ex4','ex4','ex4',True,'2022-05-31 16:08:08.725532','2022-05-31 16:08:08.725532'])

cursor.execute("INSERT INTO inventory_category (name,slug,is_active,lft,rght,tree_id,level) VALUES (%s, %s, %s, %s, %s, %s, %s)", ['Flip-Flops','flipflops', True, 1,2,1,0])

cursor.execute("INSERT INTO inventory_product_category (product_id,category_id) VALUES (%s, %s)", [8,4])

connection.queries
reset_queries()

```
