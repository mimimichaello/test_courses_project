from django.urls import path
from .views import distribute_users_to_groups_view

urlpatterns = [
    path('distribute-users/', distribute_users_to_groups_view, name='distribute_users'),
]
