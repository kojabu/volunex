from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('medic/', views.category_medical, name='medic'),
    path('sport/', views.category_sport, name='sport'),
    path('add/', views.add_event, name='add'),
    path('delete/<int:event_id>', views.delete_event, name='delete'),
    path('event/<int:event_id>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('participate/<int:event_id>/', views.participate, name='participate'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)