from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.


CAT = u'''
                  ________________________
          ∧ ∧　  /
    〜′‾‾( ﾟДﾟ) < {}
      UU‾‾U U　  \________________________
'''

def index(request):
    context = {
        "time": CAT.format( datetime.now().strftime("%I:%M %p") ),
        "numbers": list(range(10))
    }
    return render(request, "index.html", context)

def home(request):
    return render(request, "home.html")

def process(request):
    print(request.POST)
    request.session["name"] = request.POST["name"]
    return redirect("/home")