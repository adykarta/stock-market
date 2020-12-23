from django.conf.urls import url, include
from . import views
app_name = "detailStock"

urlpatterns = [
    url(r'^post-beli', views.beliSaham, name='beliSaham'),
    url(r'', views.detail, name='details')
]