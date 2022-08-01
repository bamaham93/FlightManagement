from django.shortcuts import render

# Create your views here.
def index(request):
    """
    :param request: 
    :return: 
    """
    context = {}
    return render(request, 'flight_management/index.html', context)