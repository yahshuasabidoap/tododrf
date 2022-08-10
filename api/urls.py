from django.urls import path
from . import views

urlpatterns = [
	path("", views.apiOverview, name="api-overview"),
	path("tasks", views.TaskList.as_view(), name="api-task"),
	path("tasks/<int:pk>/", views.TaskDetail.as_view(), name="api-task-detail"),
]