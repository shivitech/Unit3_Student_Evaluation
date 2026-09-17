from django.db import models


class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    section = models.CharField(max_length=20)

    django_installation = models.IntegerField(default=0)
    template_usage = models.IntegerField(default=0)
    model_and_views = models.IntegerField(default=0)
    output = models.IntegerField(default=0)

    evaluation_date = models.DateField(auto_now_add=True)

    @property
    def total_marks(self):
        return (
            self.django_installation
            + self.template_usage
            + self.model_and_views
            + self.output
        )

    @property
    def percentage(self):
        return (self.total_marks / 5) * 100

    def __str__(self):
        return f"{self.roll_number} - {self.name}"
    