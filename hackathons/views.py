from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from knohack.forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from knohack.forms import ContactForm
from knohack import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.mail import EmailMessage, send_mail
from django.core.urlresolvers import reverse #simone
from django.db import models #simone
from django.template.response import TemplateResponse



def index(request):
    return render_to_response('registration/index.html')
    #return HttpResponse("Hello, world. You're at the hackathons index.")

    
def dynpages(request):
    data = Event.objects.all()
    #data = Event.objects.get(pk=event_id)
    #return render_to_response('registration/dynpages.html')
    return TemplateResponse(request, 'registration/dynpages.html', {"data": data})
    
def alldynpages(request):
    data = Event.objects.all()
    #return render_to_response('registration/dynpages.html')
    return TemplateResponse(request, 'registration/dynpages.html', {"data": data})

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ''
    for q in latest_question_list:
        output = output + q.question_text +', '
    
    template = loader.get_template('polls/index.html')
    
    context = {
        'latest_question_list': latest_question_list,
    }
    
    return HttpResponse(template.render(context,request))
'''     
# Create your views here.

def eventpagetest(request):
        
        return render(request, 'registration/eventpagetest.html', {
        
    })

def forgotPassword(request):
    return render_to_response('registration/forgotPassword.html')


    
def howThisWorks(request):
    return render_to_response('registration/howItWorks.html')     
    
def registrationComplete(request):
    return render_to_response('registration/registrationComplete.html')  
    
def studentlogin(request):
    return render_to_response('registration/student_login.html')  
   
  

def adminSignUp(request):
    form_class = ContactForm
    if request.method == "POST":
        fname= request.POST["first_name"]
        email= request.POST["email"]
        password= request.POST["password"]
        user = User.objects.create_user(fname, email, password)
        user.save()
        return render(request, 'registration/registrationComplete.html', {
        })
    return render(request, 'registration/adminSignUp.html', {
        'form': form_class,
    })
    
    
def studentSignUp(request):
    form_class = ContactForm
    if request.method == "POST":
        fname= request.POST["first_name"]
        email= request.POST["email"]
        password= request.POST["password"]
        student = Student.objects.create_user(fname, email, password)
        student.save()
        return render(request, 'registration/registrationComplete.html', {
        })
    return render(request, 'registration/studentSignUp.html', {
        'form': form_class,
    })


@login_required
def test_Flyer(request, event_id):
    
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404('Event Not Found, Sorry Please Try Again.')
        
    return render(request, 'polls/details.html', {'question': question})


def detail(request, event_id):
    data = Event.objects.get(pk=event_id)
    return TemplateResponse(request, 'registration/dynpages.html', {"data": data})
    



'''
def detail(request, event_id):
    return HttpResponse("You're looking at question %s." % event_id)
'''
def results(request, event_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % event_id)

def vote(request, event_id):
    return HttpResponse("You're voting on question %s." % event_id)
    
    
    
    
def reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request, template_name='/reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('app:login'))


'''        
def test_Flyer(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)
'''


def reset(request):
    #password_reset(request, template_name='reset.html',
    #    email_template_name='reset_email.html',
    #    subject_template_name='reset_subject.txt')
    #    post_reset_redirect=reverse('success'))
    return render_to_response('registration/reset.html')