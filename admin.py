from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    fields = ("choice_text", "votes")
    readonly_fields = ("votes",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "is_active", "vote_count")
    list_filter = ("is_active", "pub_date")
    search_fields = ("question_text",)
    date_hierarchy = "pub_date"
    inlines = [ChoiceInline]

    @admin.display(description="Total votes")
    def vote_count(self, obj):
        return sum(choice.votes for choice in obj.choices.all())


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "question", "votes")
    list_filter = ("question",)
    search_fields = ("choice_text", "question__question_text")
    readonly_fields = ("votes",)
