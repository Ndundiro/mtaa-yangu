from . import views 
from django.urls import path
from django.conf.urls import url
# from .views import  ProjectCreateView, ProjectListView, ReviewCreateView, ProjectDetailView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   path('', views.index, name='index'), 
   path('ongeza_mtaa/', views.add_mtaa, name='add_mtaa'),
   path('<mtaa_id>/post', views.create_post, name='add_post'),
   path('mitaa/', views.mitaa, name='mitaa_zote')


   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)