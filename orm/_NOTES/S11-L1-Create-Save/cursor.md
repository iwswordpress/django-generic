# SQL Insert - Executing custom SQL Insert

```python
from inventory.models import Brand
from django.db import connection, transaction
from django.db import reset_queries

cursor = connection.cursor()
cursor.execute("INSERT INTO inventory_brand (name) VALUES (%s, %s)", ['10','Reebok'])

connection.queries
reset_queries()

```
