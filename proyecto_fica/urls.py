from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tienda import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', views.tienda, name='tienda'),  # Redirigir la raíz al método tienda
    path('tienda/', views.tienda, name='tienda'),  # Asegurarte de que la ruta tienda esté disponible
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
