from django.db import models


class BugReport(models.Model):
    smallDesc = models.TextField()
    longDesc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # automatically set the field to now when the object is first created.
    
    def __str__(self):
        return f"Bug Report {self.smallDesc} on {self.timestamp}"
