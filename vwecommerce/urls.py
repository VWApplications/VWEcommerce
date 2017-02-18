from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^produtos/', include('catalog.urls')),
    url(r'^conta/', include('accounts.urls')),
]
