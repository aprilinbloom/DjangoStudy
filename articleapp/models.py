from django.db import models


# Create your models here.
<<<<<<< HEAD

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)
<<<<<<< HEAD
=======
=======
>>>>>>> parent of 26a4e96 (djust Django course 35 commit)
>>>>>>> f0cd2593277913cb200eeba463bd4ac60b11a99e
