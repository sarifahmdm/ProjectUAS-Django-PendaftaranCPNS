from django.conf.urls import url, include
from django.contrib import admin
from mendaftar.admin import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('cpns.urls')),
    url(r'^mendaftar/', include('mendaftar.urls')),
]
