
#from django.contrib import admin
#from django.urls import include, path

#urlpatterns = [
   # path('admin/', admin.site.urls),
   # path("api/", include("application.urls"))

#]
"""
WSGI config for bookMyShow project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'bookMyShow.settings'
)

application = get_wsgi_application()
