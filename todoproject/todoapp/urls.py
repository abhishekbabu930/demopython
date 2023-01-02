from django.urls import path
from . import views
urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('class_home/', views.Todo_listview.as_view(), name='class_home'),
    path('class_detail/<int:pk>/', views.Todo_detail_view.as_view(), name='class_detail'),
    path('class_update/<int:pk>/', views.Todo_update_view.as_view(), name='class_update'),
    path('class_delete/<int:pk>/', views.Todo_delete_view.as_view(), name='class_delete'),

]
