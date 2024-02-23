from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("distroblog.urls"), name="distroblog-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("admin/", admin.site.urls),
]
