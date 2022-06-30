from . import views
from django.urls import path

from .views import GeeksCreate,GeeksList,GeeksDetailView,GeeksUpdateView,GeeksDeleteView

urlpatterns = [
    # path('',views.create_view, name='create_view'),
    # path('good',views.list_view, name='list'),
    # path('<id>',views.detail_view),
    # path('edit/<id>',views.update_view,name = 'edit'),
    # path ('<id>/delete',views.delete_view, name = 'delete'),
    
    
    path('', GeeksCreate.as_view()),
    path('jim/', GeeksList.as_view()),
    path('<pk>/', GeeksDetailView.as_view()),
    path('<pk>/update', GeeksUpdateView.as_view()),
    path('<pk>/delete/', GeeksDeleteView.as_view()),
    
    
    
   
   
    
]
