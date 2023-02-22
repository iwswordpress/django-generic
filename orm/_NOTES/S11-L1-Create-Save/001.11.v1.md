# Insert multiple objects into single table – bulk create

```python
from inventory.models import Brand
Brand.objects.all().delete()

data = [{'brand_id':3,'name': '3'},{'brand_id':4,'name': '5'}]

Brand.objects.bulk_create([Brand(**ab) for ab in data])

```
