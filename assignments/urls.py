from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'assignments'

#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:event_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:event_id>/like/', views.like, name='like'),
]

#app_name = 'assignments'
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<int:event_id>/', views.detail, name='detail'),
#	path('<int:event_id>/like/', views.like, name='like'),

    #path('<int:event_id>/results/', views.results, name='results'),
    #path('<int:event_id>/vote/', views.vote, name='vote'),
#]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)