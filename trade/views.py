from django.shortcuts import render

# Create your views here.
def trade_first(request):
    return render(request, 'trade/trade_first.html')
