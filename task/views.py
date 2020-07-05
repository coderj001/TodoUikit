from django.shortcuts import render
from django.views.generic import list
from task.models import Task

class TaskList(list.ListView):
	model=Task
	context_object_name='task'
	tamplate_name='task/task_list.html'
	def get_queryset(self, *args, **kwargs):
		qs = super(TaskList, self).get_queryset(*args, **kwargs)
		qs = qs.order_by("-task_updated")
		return qs
