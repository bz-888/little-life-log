from django.db import models

# Create your models here.
class Baby(models.Model):
    # models.CharField are called field types if you want to google others
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()# Many to Many, note Toy must be defined before we reference it
	toys = models.ManyToManyField(Toy)
	user = models.ForeignKey(User, on_delete=User)

        def get_absolute_url(self):
		# self.id refers to the cat you just created
		# this redirects the user after they created something
		# or updated the cat.
		return reverse('detail', kwargs={'cat_id': self.id})
