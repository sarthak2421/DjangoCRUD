from django.urls import path
from . import views

urlpatterns = [
    path('createView', views.createView, name='createView'),
    path('show', views.show, name='show'),
    path('edit/<int:eid>', views.edit, name='edit'),
    path('delete/<int:eid>', views.destroy, name='delete'),
    path('update/<int:eid>', views.update, name='update')
]