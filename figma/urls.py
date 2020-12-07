from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lirus/', include('lirus.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)