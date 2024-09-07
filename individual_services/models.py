import uuid
from django.db import models


class IndividualService(models.Model):
    # category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) # on_delete category, product don't delete, but set category to null
    id = models.CharField(max_length=100, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255, unique=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    number_hours = models.IntegerField(default=0)
    duration_weeks = models.IntegerField(default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name