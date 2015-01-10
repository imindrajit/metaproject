from django.db import models

# Create your models here.
class website(models.Model):
	link = models.CharField(blank=False,max_length=50)
	title = models.CharField(blank=False,max_length=500)
	timestamp = models.CharField(blank=False,max_length=100)
	meta = models.TextField(blank=True)

	
	def __unicode__(self):
		return '%s' % (self.link)



	class Meta:
		ordering = ['link']
		db_table = 'pages'
