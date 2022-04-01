from django.urls import re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^addmodel', views.addmodel, name="addmodel"),
    re_path(r'^createmodel$', views.createmodel, name="createmodel"),
    re_path(r'^$', views.base, name='base'),
    re_path(r'^admin_models$', views.admin_models, name='admin_models'),
    re_path(r'^admin_current_models$', views.admin_current_models, name='admin_current_models'),
    re_path(r'^delete/(?P<id>\d+)$', views.delete,name="delete"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)