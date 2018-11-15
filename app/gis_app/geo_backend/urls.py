from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.default_map, name="default"),
    # url(r'^polygon/(?P<lon>-?\d+.?\d+)/(?P<lat>-?\d+.?\d+)/$', views.get_polygon, name="polygon"),
    url(r'polygon/', views.get_polygon, name="polygon"),
    url(r'surroundings/', views.get_surroundings, name="surroundings"),
    url(r'all_plants/', views.get_all_buffers, name="all_plants")
]
