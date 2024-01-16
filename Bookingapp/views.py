from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import BookingForm
from .models import Menu


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def index(request):
    render(request, 'index.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {
        "menu" : menu_data
    }
    render(request,'menu.html',{"menu": main_data})

def display_menu_item(request,pk):
    if pk:
        menu_item = objects.get(pk=pk)
    else:
        menu_item=''
    render(request, 'menu_item.html', {"menu_item": menu_item})