# Insert into single table with create()

```python
from inventory.models import Brand, Category
from django.db import connection
from django.db import reset_queries

x = Brand.objects.create(brand_id=1,name='nike')

x = Category.objects.create(name='Trainers', slug='trainers', is_active=True)

connection.queries
reset_queries()
```