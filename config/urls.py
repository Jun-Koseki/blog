from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
