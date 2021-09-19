from django.db import models

class Images(models.Model):
    image_name = models.CharField(max_length=100)
    image_file = models.ImageField()

    image_type_choices = (
        ('Nature', 'Nature'), 
        ('Space', 'Space'), 
        ('Urban', 'Urban'), 
        ('Abstract', 'Abstract')
        )

    image_type = models.CharField(max_length=10, choices=image_type_choices)