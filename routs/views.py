from django.contrib import messages
from django.shortcuts import render
from routs.forms import RoutForm
from routs.utils import get_routs

# Create your views here.
def home(request):
    form = RoutForm()
    return render(request, 'routs/home.html', context={'form': form})


def find_routs(request):
    if request.method == 'POST':
        form = RoutForm(request.POST)
        if form.is_valid():
            try:
                context = get_routs(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routs/home.html', context={'form': form})
            return render(request, 'routs/home.html', context=context)
        return render(request, 'routs/home.html', context={'form': form})
    else:
        form = RoutForm()
        messages.error(request, 'Wrong data')
        return render(request, 'routs/home.html', context={'form': form})

