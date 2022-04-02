from django.urls import path
from .views import (
    index,
    update,
    delete
)

urlpatterns = [
    path('',index,name="index"),
    path('update/<int:id>/',update,name="update_task"),
    path('delete/<int:id>/',delete,name="delete_task")
]
