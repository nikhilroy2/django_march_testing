from django.shortcuts import render,redirect
import string, random
from .models import URL
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt
from .forms import create_forms
from .models import CRUD_Create
from django.contrib.auth.models import User
print(User)
# Create your views here.
def Index(request):
    if request.method == 'POST':
        create = create_forms(request.POST)
        if create.is_valid():
            create.save()
            return redirect('/')
    else:
        create = create_forms()
    context = {
    "create_forms": create,
    "view_forms": CRUD_Create.objects.all().order_by('-id')
    }
    print(context)
    return render(request, 'index.html', context=context)


def edit(request, pk):
    post = CRUD_Create.objects.filter(pk=pk)
    if request.method == 'POST':
        create = create_forms(request.POST)
        if create.is_valid():
            create.save()
            return redirect('/')
    else:
        create = create_forms()
    return render(request, 'update.html', {"post": post, "create": create})
def delete(request, pk):
    post = CRUD_Create.objects(pk=pk)
    post.remove()
    return redirect('/')
#............................url shorter testing..................
    
