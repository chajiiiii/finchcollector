from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch

from .forms import FeedingForm

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

    feeding_form = FeedingForm()
    return render(request, "finches/detail.html", { 'finch' : finch, 'feeding_form': feeding_form})

class FinchCreate(CreateView):
    model = Finch
    fields = "__all__"

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['wingspan', 'colors']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


def finches_delete(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    finch.delete()
    return redirect('index')

def add_feeding(request, finch_id):
    # Create a modelForm instance using the data that was submitted in the form
    form = FeedingForm(request.POST)

    # Validate the form
    if form.is_valid():
        # Don't save the form to the DB until it has the finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)