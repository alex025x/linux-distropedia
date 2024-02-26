from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("distroblog.urls")),  # Move this line after the admin pattern
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
