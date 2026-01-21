from django.urls import path
from .views import (
    DatasetListCreateView,
    DatasetDetailView,
    DataElementListCreateView
)

urlpatterns = [
    path('datasets/', DatasetListCreateView.as_view()),
    path('datasets/<int:pk>/', DatasetDetailView.as_view()),
    path('datasets/<int:dataset_id>/elements/', DataElementListCreateView.as_view()),
]
