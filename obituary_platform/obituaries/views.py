from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Obituary

def submit_obituary(request):
    if request.method == 'POST':
        obituary = Obituary(
            name=request.POST['name'],
            date_of_birth=request.POST['date_of_birth'],
            date_of_death=request.POST['date_of_death'],
            content=request.POST['content'],
            author=request.POST['author']
        )
        obituary.save()
        return redirect('confirmation')  # Redirect to a confirmation page
    return render(request, 'obituary_form.html')

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'obituary_list.html', {'obituaries': obituaries})

def home(request):
    return render(request, 'home.html')

def landing_page(request):
    return render(request, 'landing_page.html')

class ObituaryListView(ListView):
    model = Obituary
    template_name = 'obituaries/obituary_list.html'
def confirmation(request):
    return render(request, 'confirmation.html')
