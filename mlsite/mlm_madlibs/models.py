from django.db import models

class MLM_text(models.Model):
    text=models.CharField(max_length=255)