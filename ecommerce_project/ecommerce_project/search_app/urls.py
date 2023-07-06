app_name = "search_app"

from django.urls import path
from search_app import views

urlpatterns = [
    # other URL patterns
    path('search/', views.SearchResult, name='search_result'),
]
