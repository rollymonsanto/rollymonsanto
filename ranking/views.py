from django.shortcuts import render
from .models import Score
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    ranks = Score.objects.filter().extra(
        select={'rank': 'DENSE_RANK() OVER(ORDER BY score DESC, target_hit DESC)'}
    ).order_by('-score', 'rank', 'date_played')[:10]
    last_scores = Score.objects.filter().extra(
        select={'rank': 'DENSE_RANK() OVER(ORDER BY score DESC, target_hit DESC)'}
    ).order_by('-date_played')[:3]

    context = {
        "ranks": ranks,
        "lastscores": last_scores,
    }
    return render(request, 'ranking/index.html', context)


@login_required
def new_player(request):
    form = PlayerForm

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        "form": form,
    }
    return render(request, 'ranking/player.html', context)
