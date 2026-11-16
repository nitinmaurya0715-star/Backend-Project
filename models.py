from django.db import models
from django.utils import timezone


class Question(models.Model):
    """A poll question and its publication/closing dates."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Poll question"
        verbose_name_plural = "Poll questions"

    def __str__(self):
        return self.question_text

    @property
    def is_open(self):
        return self.is_active


class Choice(models.Model):
    """An answer option belonging to a question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.choice_text
