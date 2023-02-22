# Explore the difference between save() and create()

```python
from inventory.models import Brand, Category
from django.db import connection, reset_queries

Brand.objects.all().delete()
Brand.objects.create(brand_id=1,name="nike")

Brand(brand_id=1000,name="nike1000").save()

Category.objects.all().delete()

Category.objects.create(id=3, name='Trainers', slug='trainers', is_active=True)

x = Category(id=3, name='Trainers100', slug='trainers1000', is_active=True)
x.save()

connection.queries
reset_queries()

Category.objects.create(name='Trainers1000', slug='trainers1000', is_active=True)

```
