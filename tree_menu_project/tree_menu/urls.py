from django.urls import path
from tree_menu.views import PageView

app_name = 'tree_menu'

urlpatterns = [
    path('', PageView.as_view(), name='index')
]
