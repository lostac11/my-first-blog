from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
      author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
      title = models.CharField(max_length = 200)
      text = models.TextField()
      creted_date = models.DateTimeField(default = timezone.now)
      published_date = models.DateTimeField(blank = True, null = True)
      def publish(self):
          self.published_date = timezone.now()
          self.save()
      def __dir__(self):
         return  self.title
