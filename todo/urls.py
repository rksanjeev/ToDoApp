from django.urls import path
import todo.views as views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='home' ),
    path('update/<int:pk>', views.update_task, name='update'),
    path('delete/<int:pk>', views.delete_task, name='delete'),

]
