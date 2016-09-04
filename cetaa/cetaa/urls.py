from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from about1.views import about_index


urlpatterns = [
    # Home
	url(r'^$', index),
    # About views
	url(r'^about', about_index),
    # Admin views
    url(r'^admin/', admin.site.urls),
]