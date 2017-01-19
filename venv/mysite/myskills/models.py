from django.db import models

# Create your models here.
class Skills(models.Model):
	name=models.CharField(max_length=500)
	level=models.IntegerField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural='Skills'
