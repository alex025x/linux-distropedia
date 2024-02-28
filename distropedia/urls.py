from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from distroblog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("distroblog.urls")),  # Move this line after the admin pattern
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("", views.PostList.as_view(), name='home'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
