from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.conf import settings
import md5

from .models import Url, View

@login_required()
def index(request):
    url_list = Url.objects.filter(user=request.user).order_by('-id')
    context = {
        'url_list': url_list,
    }
    if request.method == 'POST':
        url_hash = md5.new(request.POST['url'])
        url_hash.update(unicode(request.user.pk))
        url_hash.update(settings.SECRET_KEY)
        url_hash = url_hash.hexdigest()
        try:
            url = Url.objects.get( hash = url_hash)
            context['current'] = url.pk
        except Url.DoesNotExist:
            try:
                url = Url(url = request.POST['url'], user = request.user, hash = url_hash)
                url.full_clean()
                url.save()
                context['current'] = url.pk
            except ValidationError as e:
                context['errors'] = e.messages[0]
    return render(request, 'urls/index.html', context)

def shortcut(request, hash_param):
    if not request.session.exists(request.session.session_key):
        request.session.create() 

    url_item = get_object_or_404(Url, hash=hash_param)
    view = View(session_id = request.session.session_key, url = url_item)
    view.save()
    
    return redirect(url_item.url)
