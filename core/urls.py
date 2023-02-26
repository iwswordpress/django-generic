from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("authuser/", include("authuser.urls")),
    path("admin/", admin.site.urls),
    # path("cbv/", include("cbv.urls", namespace="cbv")),
    path("crm/", include("crm.urls", namespace="crm")),
    path("csvs/", include("csvs.urls", namespace="csvs")),
    path("forms/", include("forms.urls", namespace="forms")),
    # path("htmx/", include("htmx.urls", namespace="htmx")),
    # path("orm/", include("orm.urls", namespace="orm")),
    # path("middleware/", include("middleware.urls", namespace="middleware")),
    # path("projects/", include("projects.urls", namespace="projects")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
