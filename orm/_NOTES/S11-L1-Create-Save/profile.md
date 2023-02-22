# Query Profiling - bulk_create vs create performance 

```python
from inventory.models import Brand
from django.db import connection, transaction
from django.db import reset_queries
import cProfile

# from inventory import views

def using_multiple_inserts():
    for n in range(10000):
        Brand.objects.create(name=f"{n}")

p = cProfile.Profile()
p.runcall(using_multiple_inserts)
p.print_stats(sort='tottime')

def using_bulk_create():
    Brand.objects.bulk_create([Brand(name=f"{n}") for n in range(10000)])

p = cProfile.Profile()
p.runcall(using_bulk_create)
p.print_stats(sort='tottime')


Brand.objects.all().delete()
connection.queries
reset_queries()

```