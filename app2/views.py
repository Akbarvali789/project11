from django.shortcuts import render

# Create your views here.
def okjanu(request):
    return render(request,'a2_first.html')

def raabta(request):
    return render(request,'a2_second.html')
