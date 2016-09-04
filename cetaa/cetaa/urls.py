from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from about1.views import about_index
from cetaa.views import register, registration_complete, loggedin
from django.contrib.auth.views import login, logout


urlpatterns = [
    # Home
	url(r'^$', index),
    # About views
	url(r'^about', about_index),
    # Accounts views
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^accounts/register/complete/$', registration_complete, name='registration_complete'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/loggedin/$', loggedin, name='loggedin'),
    # Admin views
    url(r'^admin/', admin.site.urls),
]