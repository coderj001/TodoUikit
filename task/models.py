from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Task(models.Model):
	task_id=models.AutoField(
		primary_key=True,
		editable=False
		)
	task_title=models.CharField(
		max_length=255,
		blank=False,
		verbose_name='Title'
		)
	task_desciption=models.TextField(
		blank=True,
		null=True,
		verbose_name='Desciption'
		)
	task_created=models.DateTimeField(auto_now_add=True,
		editable=False,
		verbose_name='Date on create'
		)
	task_updated=models.DateTimeField(auto_now=True,
		editable=True,
		verbose_name='Date on update'
		)
	task_status=models.BooleanField(default=False)
	task_user=models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		if len(self.task_title) < 10:
			return f'{self.task_id} - {self.task_title}'
		else:
			return f'{self.task_id} - {self.task_title[:10]}..'
	def get_absolute_url(self):
		return reverse('task:taskdetail', kwargs={'pk':self.task_id})
