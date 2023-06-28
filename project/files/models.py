from django.db import models


# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def mark_as_processed(self):

        self.processed = True
        self.save()
