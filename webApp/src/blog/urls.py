from django.urls import path

from .views import (
   blogpost_detail_view,
   blogpost_list_view,
   blogpost_create_view,
   blogpost_delete_view,
   blogpost_update_view)


urlpatterns = [
    # blog
    path('', blogpost_list_view),

    path('<str:slug>/', blogpost_detail_view, name='detail'),
    path('<str:slug>/edit/', blogpost_update_view),
    path('<str:slug>/delete/', blogpost_delete_view),

]
