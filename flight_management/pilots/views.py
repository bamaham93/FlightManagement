from django.shortcuts import render

# Create your views here.
def index(request):
    """
    :param request:
    :return:
    """
    context = {}
    return render(request, 'pilots/index.html', context)