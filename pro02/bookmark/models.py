from django import models

class Bookmark(models.Model):
    id = models.ObjectIdField()
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')
