from django.shortcuts import render

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
    return render(request, "finches/index.html", {
        "finches": finches
    })