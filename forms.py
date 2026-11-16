from django import forms
from .models import Choice


class VoteForm(forms.Form):
    """Radio-button form that validates a choice belongs to the selected question."""
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None,
        error_messages={"required": "Please select one option before submitting."},
        label="Choose one option",
    )

    def __init__(self, *args, question, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = question
        self.fields["choice"].queryset = question.choices.all()

    def clean_choice(self):
        choice = self.cleaned_data["choice"]
        if choice.question_id != self.question.pk:
            raise forms.ValidationError("That option does not belong to this question.")
        return choice
