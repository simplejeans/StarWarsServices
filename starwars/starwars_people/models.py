from django.db import models


class Dataset(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to="datasets/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
