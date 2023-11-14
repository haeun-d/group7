from django.shortcuts import render

# Create your views here.
def main_consumption(request):
    return render(request, 'consumption/main_consumption.html')