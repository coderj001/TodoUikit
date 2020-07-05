from django.urls import path
from task.views import (
		TaskList,
	)
app_name='task'

urlpatterns = [
	path('',TaskList.as_view(),name='tasklist')
]
