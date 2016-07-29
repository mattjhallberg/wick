from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.home.urls')),
    url(r'^entry', include('apps.entry.urls'))
]