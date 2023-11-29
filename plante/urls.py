from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from appPlante.views import BASE, PlanteViewset, SalleViewset, NodeViewset, MeasureViewset

router = routers.SimpleRouter()
router.register('plante', PlanteViewset, basename='plante')
router.register('salle', SalleViewset, basename='salle')
router.register('node', NodeViewset, basename='node')
router.register('measure', MeasureViewset, basename='measure')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', BASE, name='home'),  # Modification ici pour utiliser BASE pour l'URL racine
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
