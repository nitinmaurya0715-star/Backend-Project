from django.contrib import messages
from django.db.models import F
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import VoteForm
from .models import Question


def index(request):
    """Show published questions; future-dated questions are not displayed."""
    questions = Question.objects.filter(
        is_active=True, pub_date__lte=timezone.now()
    ).prefetch_related("choices")
    return render(request, "polls/index.html", {"questions": questions})


def detail(request, question_id):
    """Display one question and its validated voting form."""
    question = get_object_or_404(
        Question, pk=question_id, is_active=True, pub_date__lte=timezone.now()
    )
    form = VoteForm(question=question)
    return render(request, "polls/detail.html", {"question": question, "form": form})


@require_POST
def vote(request, question_id):
    """Accept votes only through POST and increment a valid choice atomically."""
    question = get_object_or_404(
        Question, pk=question_id, is_active=True, pub_date__lte=timezone.now()
    )
    form = VoteForm(request.POST, question=question)
    if form.is_valid():
        # F() performs the increment in the database and avoids lost updates.
        from .models import Choice
        Choice.objects.filter(pk=form.cleaned_data["choice"].pk).update(
            votes=F("votes") + 1
        )
        messages.success(request, "Your vote has been recorded.")
        return redirect("polls:results", question_id=question.pk)

    messages.error(request, "Please correct the form and try again.")
    return render(request, "polls/detail.html", {"question": question, "form": form}, status=400)


def results(request, question_id):
    """Display the current totals and percentage for each option."""
    question = get_object_or_404(Question, pk=question_id)
    choices = list(question.choices.all())
    total_votes = sum(choice.votes for choice in choices)
    for choice in choices:
        choice.percentage = round(choice.votes * 100 / total_votes, 1) if total_votes else 0
    return render(request, "polls/results.html", {
        "question": question, "choices": choices, "total_votes": total_votes
    })
