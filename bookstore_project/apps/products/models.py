from django.db import models

# Create your models here.
class Book(models.Model):
    code = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    isbn = models.CharField(unique=True, max_length=13, blank=False, null=False)

    class Meta:
    	unique_together = (('title', 'author'),)

    def __str__(self):
        return self.title

class Author(models.Model):
	code = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250, blank=False, null=False)

	def __str__(self):
		return self.name
