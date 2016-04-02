from django.shortcuts import render

# Create your views here.
def about(request):
  return render(request, 'pgopen/templates/pages/about.html', {'page':''})

def becomesponsor(request):
  return render(request, 'pgopen/templates/pages/becomesponsor.html', {'page':''})

def blog(request):
  return render(request, 'pgopen/templates/pages/blog.html', {'page':''})

def papers(request):
  return render(request, 'pgopen/templates/pages/callforpapers.html', {'page':''})

def index(request):
  return render(request, 'pgopen/templates/pages/index.html', {'page':'landing'})

def policies(request):
  return render(request, 'pgopen/templates/pages/policies.html', {'page':''})

def schedule(request):
  return render(request, 'pgopen/templates/pages/schedule.html', {'page':''})

def social(request):
  return render(request, 'pgopen/templates/pages/social.html', {'page':''})

def sponsors(request):
  return render(request, 'pgopen/templates/pages/sponsors.html', {'page':''})

def become_sponsor(request):
  return render(request, 'pgopen/templates/pages/becomesponsor.html', {'page':''})

def tickets(request):
  return render(request, 'pgopen/templates/pages/tickets.html', {'page':''})

def venue(request):
  return render(request, 'pgopen/templates/pages/venue.html', {'page':''})