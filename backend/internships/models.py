from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class InternshipPlacement(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_placements'
    )
    supervisor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supervisor_placements'
    )
    organization_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.organization_name}"

# Create your models here.
