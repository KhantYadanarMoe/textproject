from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.contrib import messages

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('enroll.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['father']
  d = request.POST['dob']
  e = request.POST['nrc']
  f = request.POST['contact']
  g = request.POST['email']
  h = request.POST['address']
  i = request.POST['edu']
  if (a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i==""):
    messages.info(request, "All fields are required!")
    return HttpResponseRedirect(reverse('add'))

  else:
    member = Members(firstname = a, lastname = b, fathername = c, dateofbirth = d, nrcno = e, contactno= f, emailAddress = g, pAddress = h, edu = i)
    member.save()
    messages.info(request, 'You have successfully enrolled!')
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  father = request.POST['father']
  dob = request.POST['dob']
  nrc = request.POST['nrc']
  contact = request.POST['contact']
  email = request.POST['email']
  address = request.POST['address']
  edu = request.POST['edu']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.fathername = father
  member.dateofbirth = dob
  member.nrcno = nrc
  member.contactno = contact
  member.emailAddress = email
  member.pAddress = address
  member.edu = edu
  member.save()
  return HttpResponseRedirect(reverse('index'))