from django.db import models
import datetime
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150, verbose_name="title")
    description = models.TextField(blank=True)
    f_creation = models.DateField(default=datetime.date.today)
    creation_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    
    
        #self.a.strftime('%Y-%m-%d %H:%M:%S')
        
    
    def __str__(self):
        return self.title   