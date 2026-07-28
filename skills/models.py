from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('design', 'Design'),
        ('tools', 'Tools'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=0, help_text="0-100, used for progress bar width")
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    is_tool = models.BooleanField(default=False, help_text="Split skills vs tools sections")
    order = models.IntegerField(default=0, help_text="Lower numbers show first")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
