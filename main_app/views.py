from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView

from .models import Finch

# finches = [
#   {'breed': 'European Goldfinch', 'wingspan': '21cm to 25.5cm', 'colors': "red, black, yellow"},
#   {'breed': 'Chaffinch', 'wingspan': '26cm', 'colors': "grey, brown, yellow"},
#   {'breed': 'Greenfinch', 'wingspan': '21cm to 25.5cm', 'colors': "grey, black, yellow"},
#   {'breed': 'Linnet', 'wingspan': '21cm to 25.5cm', 'colors': "red, brown, grey"},
# ]

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {
        "finches": finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, "finches/detail.html", { 'finch' : finch })

class FinchCreate(CreateView):
    model = Finch
    fields = "__all__"

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['wingspan', 'colors']