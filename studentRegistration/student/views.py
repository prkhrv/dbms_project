from django.shortcuts import render,redirect
from .models import student
from .forms import studentForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        try:
            search1 = request.POST.get('username')
            search2 = student.objects.filter(name=search1)
            search3 = search2.values_list('name','gender','fname',
                        'roll','email','phone',
                        'branch','address').get()
            return render(request, 'details.html',{'search3':search3})
        except student.DoesNotExist:
            return render(request,'error.html')
    return render(request,"home.html")

def register(request):
    form = studentForm
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            return render(request,'error.html')
    return render(request, "form.html")
