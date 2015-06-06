from django.shortcuts import render
from django.contrib import messages

# Create your views here.

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import RequestContext
from .forms import HomelessPeopleForm, DonatorsForm

def home(request):

    return render_to_response("index.html",
                              locals(),
                              context_instance=RequestContext(request))


def homeless(request):

    form = HomelessPeopleForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit = False)
        save_it.save()
        messages.success(request, "Thank you, Start playing",)
        return HttpResponseRedirect('/')

    return render_to_response("homeless.html",
                              locals(),
                              context_instance=RequestContext(request))


def donators(request):

    form = DonatorsForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit = False)
        save_it.save()
        messages.success(request, "Thank you, Start playing",)
        return HttpResponseRedirect('/')

    return render_to_response("donators.html",
                              locals(),
                              context_instance=RequestContext(request))


def search(request):

    if request.POST:

	    print request.POST['term']
	    return HttpResponseRedirect("/")

    else:
	    return render_to_response('search.html')
