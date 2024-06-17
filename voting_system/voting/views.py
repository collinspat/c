from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from.models import Candidate, Election, Vote

# Create your views here.
@login_required
def voter_panel(request):
    elections = Election.objects.all()
    return render(request, 'voter_panel.html', {'elections': elections})
    pass

@login_required
def admin_panel(request):
    elections = Election.objects.all()
    return render(request, 'admin_panel.html', {'elections': elections})
    pass

@login_required
def cast_vote(request):
    if request.method == 'POST':
        candidate_id = request.POST['candidate']
        candidate = Candidate.objects.get(id=candidate_id)
        position = candidate.position
        voter = request.user
        vote = Vote(voter=voter, candidate=candidate, position=position)
        vote.save()
        return redirect('voter_panel')
    else:
        candidates = Candidate.objects.all()
        return render(request, 'cast_vote.html', {'candidates': candidates})
    pass

@login_required
def view_vore(request):
    votes = Vote.objects.filter(voter=request.user)
    return render(request, 'view_vote.html', {'votes': votes})
    pass    
