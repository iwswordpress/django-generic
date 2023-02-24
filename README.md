### DJANGO-GERNERIC

YouTube video seres: to follow...

The best bits and practices from a wiode variety of resources, training and work all wired into one complete application.

Some apps have their own set of models and others have both their own and acces to other app models.

### FEATURED APPS

- async: using async methods.
- authUser: use email for login with signals creating a OneToOne Profile model. _See note below about replacing User with settings.AUTH_USER_MODEL_.
- blog: standard posts with avatar uploads, followeres, likes etc.
- cbv: class based views.
- crm: dashboard app with many CRUD utilities.
- csvs: upload csvs, read, store in DB and process with pandas etc.
- forms: a variety of forms with validation.
- htmx: using HTMX to provide slient side reactivity without JavaScript.
- middleware: create our own custom middleware.
- orm: a deeper dive into Django ORM.
- plots: using various libararies to create plots, charts, etc.
- projects: a functional CRUD that includes file (image) upload. Some fields are based on another model.

For User uses settings.AUTH_USER_MODEL as we have defined in core/settings.py:

```
AUTH_USER_MODEL = "authuser.User"
```
This uses email/password login for app and admin login.