from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token as oat
from api import views


router = routers.DefaultRouter()
router.register(r'managers', views.ManagerViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', oat),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
