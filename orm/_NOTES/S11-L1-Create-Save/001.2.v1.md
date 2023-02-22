# Insert into single table with save()

```python
Model.save(force_insert=False, force_update=False, using=DEFAULT_DB_ALIAS, update_fields=None)

from inventory.models import Brand, Category
Brand.objects.all()
Brand.objects.all().delete()

x = Brand(brand_id=1000)
x.name="nike1000"
x.save()

x = Category(name="trainers1", slug="trainers1", is_active=True)
x.save()

Category.objects.all()

```
