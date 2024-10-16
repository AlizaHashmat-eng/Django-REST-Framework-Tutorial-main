from django.urls import include, path
from rest_framework import routers
from drf_tutorial.quickstart import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),  
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]