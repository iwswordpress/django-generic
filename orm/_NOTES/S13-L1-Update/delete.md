# Delete single object

```python
from inventory.models import Brand
from django.db import connection
from django.db import reset_queries

x = Brand.objects.create(name='Adidas')

Brand.objects.all().delete()

Brand.objects.get(brand_id=1).delete()

Brand.objects.filter(brand_id_2).delete()

# Note sign-posting to FK behavior (possible future referral to Django ORM course focused on building databases/structure)

connection.queries
reset_queries()

```
