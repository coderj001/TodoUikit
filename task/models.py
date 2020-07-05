from django.db import models

COLOR_CHOICE=(
		('BLACK','black'),
		('BLUE','blue'),
		('RED','red'),
		('GREEN','green'),
		('YELLOW','yellow'),
		('WHITE','white'),
	)

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
	task_color=models.CharField(
		choices=COLOR_CHOICE,
		max_length=6,
		default='WHITE'
		)
	task_status=models.BooleanField(default=False)
	def __str__(self):
		if len(self.task_title) < 10:
			return f'{self.task_id} - {self.task_title}'
		else:
			return f'{self.task_id} - {self.task_title[:10]}..'
	def get_absolute_url(self):
		pass
