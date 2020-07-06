from django.urls import path
from task.views import (
		TaskList,
		TaskDetail,
		change_task_status,
		delete_task,
		update_task,
		add_task,
		delete_task,
		user_login,
		user_logout,
		sign_up
	)
app_name='task'

urlpatterns = [
	path('',TaskList.as_view(),name='tasklist'),
	path('taskdetail/<pk>/',TaskDetail.as_view(),name='taskdetail'),
	path('edit/<id>/',change_task_status,name='edit'),
	path('delete/<id>/',delete_task,name='delete'),
	path('update/<id>/',update_task,name='update'),
	path('delete/<id>/',delete_task,name='delete'),
	path('add/',add_task,name='add'),
	path('login/',user_login,name='login'),
	path('logout/',user_logout,name='logout'),
	path('signup/',sign_up,name='signup'),
]
