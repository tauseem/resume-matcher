from django.db import models

class Analysis(models.Model):
    job_title = models.CharField(max_length=100)
    resume_text = models.TextField()
    job_description = models.TextField()
    score = models.FloatField(default=0)
    missing_keywords = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)