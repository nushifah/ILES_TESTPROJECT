from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

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

    def clean(self):
        # Rule 1: end date must be after start date
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be earlier than start date.")

        # Rule 2: selected student must really be a student
        if self.student.role != 'student':
            raise ValidationError("Selected user for student must have the student role.")

        # Rule 3: selected supervisor must really be a workplace supervisor
        if self.supervisor.role != 'workplace_supervisor':
            raise ValidationError("Selected user for supervisor must have the workplace supervisor role.")

        # Rule 4: prevent overlapping placements for the same student
        overlapping = InternshipPlacement.objects.filter(
            student=self.student,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("This student already has an overlapping internship placement.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
