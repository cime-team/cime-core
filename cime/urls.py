"""
Enrutador de CIME-Core

En este archivo, cada aplicación que esté en una capa superior a Core deberá
definir sus urls como parte del router:
    from accounts.views import AccountViewSet
    router.register(r'accounts', AccountViewSet)
el módulo urls deberá estar definido dentro de cada aplicación.

documentación:
http://www.django-rest-framework.org/api-guide/routers/
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

# Enrutador de DRF
router = DefaultRouter()
#router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
