from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
        url(r'^$',views.showpage,name='galeria'),
        url(r'^search/', views.search_category, name='search_category'),
        url('^image/(?P<image_id>\d+)/$',views.image_properties, name='image'),

]