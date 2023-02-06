from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    context = {
        'variable':'temp'
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")
    # return HttpResponse("this is the about")

@csrf_exempt
def contact(request):
    if request.method == "POST":
       #Redundant Values(default provided)
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        #Input Values from Frontend
        date = request.POST.get("date")
        time = request.POST.get("time")
        reaction = request.POST.get("reaction")
        print(name, email, password, date, str(int(reaction)),time)
        # datef =datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        contact = Contact(name = name, email = email, password = password, reaction = int(reaction), date = date,time = time)
        contact.save()
    return HttpResponse('')