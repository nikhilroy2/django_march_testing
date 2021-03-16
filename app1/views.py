from django.shortcuts import render,redirect
import string, random
from .models import URL
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt
import redis
rds = redis.Redis(host="localhost", port=6379, db=0)
# Create your views here.
def Index(request):
    current_site = get_current_site(request)
    return render(request, 'index.html')

    
@csrf_exempt
def short_url(request):
    long_url = request.POST.get("url")
    current_site = get_current_site(request)
    data = {
        "success": True,
        "link": "http://{}/{}".format(current_site, hash),
        "long_url": long_url
    }
    return JsonResponse(data)


def shortit(long_url):
    # hash length
    N = 7
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # generate a random string of length 7
    url_id = ''.join(random.choices(s, k=N))
    # check the hash id is in
    if not URL.objects.filter(hash=url_id).exists():
        # create a new entry for new one
        create = URL.objects.create(full_url=long_url, hash=url_id)
        return url_id
    else:
        # if hash id already exists create a new hash
        shortit(url)



def redirector(request,hash_id=None):
    # get the value from redis key, if value not in return None
    hash_code = rds.get(hash_id)
    if hash_code is not None:
        return redirect(hash_code.decode('ascii'))

    if URL.objects.filter(hash=hash_id).exists():
        url = URL.objects.get(hash=hash_id)
        # set the value in redis for faster access
        rds.set(hash_id,url.full_url)
        # redirect the page to the respective url
        return redirect(url.full_url)
    else:
        # if the give key not in redis and db
        return JsonResponse({"success":False})