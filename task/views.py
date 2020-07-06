from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView
from task.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

class TaskList(ListView):
	model=Task
	context_object_name='tasks'
	tamplate_name='task/task_list.html'
	def get_queryset(self, *args, **kwargs):
		qs = super(TaskList, self).get_queryset(*args, **kwargs)
		if self.request.user.is_authenticated:
			qs = qs.filter(task_user=self.request.user)
		qs = qs.order_by("-task_updated")
		return qs
	# @login_required
	# def dispatch(self, request, *args, **kwargs):
	# 	return super(TaskList, self).dispatch(request, *args, **kwargs)

class TaskDetail(DetailView):
	model=Task
	context_object_name='task'
	template_name='task/task_detail.html'

def change_task_status(req,id):
	task=get_object_or_404(Task,task_id=id)
	if task is not None:
		if task.task_status:
			task.task_status=False
		else:
			task.task_status=True
		task.save()
	return redirect('task:tasklist')

def delete_task(req,id):
	task=get_object_or_404(Task, task_id=id)
	if task is not None:
		task.delete()
	return redirect('task:tasklist')

def update_task(req,id):
	if req.method == 'POST':
		task=get_object_or_404(Task,task_id=id)
		if req.POST['task_title'] is not None or req.POST['task_desciption'] is not None:
			task.task_title=req.POST['task_title']
			task.task_desciption=req.POST['task_desciption']
			task.save()
		return redirect('task:tasklist')

def add_task(req):
	if req.method == 'POST':
		task=Task.objects.create(
			task_title=req.POST['task_title'],
			task_desciption=req.POST['task_desciption'],
			task_user=req.user,
			)
		task.save()
		return redirect('task:tasklist')

def delete_task(req,id):
	task=get_object_or_404(Task,task_id=id)
	if task is not None:
		task.delete()
		return redirect('task:tasklist')

def user_login(req):
	if req.method == 'POST':
		user = authenticate(username=req.POST['username'], password=req.POST['password'])
		if user is not None:
			login(req,user)
			return redirect('task:tasklist')
		else:
			pass

def user_logout(req):
	logout(req)
	return redirect('task:tasklist')

def sign_up(req):
	if req.method == 'POST':
		form = UserCreationForm(req.POST)
		if form.is_valid():
			user = form.save()
			login(req,user)
			return redirect('task:tasklist')
	else:
		form = UserCreationForm()
	return render(req, 'account/signup.html', {'form': form})
