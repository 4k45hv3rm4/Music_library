from django.shortcuts import render, get_object_or_404
from .models import CD
def index(request):
    cd_info = CD.objects.all()
    return render(request,
                'cd_library/index.html',
                {'cd_info':cd_info})


def detail(request, id):
    cd_detail = get_object_or_404(CD, id=id)
    return render(request,
                'cd_library/detail.html',
                {'cd_detail':cd_detail})


