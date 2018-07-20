from django.conf.urls import url
from .import views

urlpatterns = [
        url(r'create/$',views.post_create,name = 'postcreate'),
        url(r'(?P<id>\d+)/$',views.post_detail,name = 'postdetail'),
        url(r'(?P<id>\d+)/delete/$',views.post_delete,name = 'postdelete'),
        url(r'(?P<id>\d+)/edit/$',views.post_update,name = 'postupdate'),
        url(r'^$',views.post_list,name = 'postslist'),
        ]
