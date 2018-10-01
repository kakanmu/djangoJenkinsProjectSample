from django.db import models

# Create your models here.

class BaseAppModels(models.Model):
 name = models.CharField(max_length=500, null=True, blank=True)
 description = models.TextField(max_length=500, null=True, blank=True)
 is_active = models.BooleanField(default=True)
 creation_date = models.DateTimeField(auto_now_add=True, editable=False, null=True)
 modified_date = models.DateTimeField(auto_now=True, editable=False, null=True)

 def __str__(self):
  return self.name

 class Meta:
  ordering = ["name"]
