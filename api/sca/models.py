from django.db import models

class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Mission(models.Model):
    cat = models.OneToOneField(SpyCat, on_delete=models.PROTECT, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name if self.cat else 'Unassigned'}"

    def save(self, *args, **kwargs):
        if self.is_completed and self.cat:
            self.cat.is_available = True
            self.cat.save()
            self.cat = None

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.cat:
            raise ValueError("Cannot delete a mission that is assigned to a cat.")
        super().delete(*args, **kwargs)

class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_complete and self.pk:
            original = Target.objects.get(pk=self.pk)
            if original.notes != self.notes:
                raise ValueError("Cannot update notes for a completed target.")
        super().save(*args, **kwargs)
