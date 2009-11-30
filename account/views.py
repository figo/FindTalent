# Create your views here.
from django.shortcuts import render_to_response
from django.http      import HttpResponseRedirect
from FindTalent.account.models import TalentUser
import hashlib

def get_empty_val_checker( dic ):
  return ( lambda key: ( dic.has_key( key ) and dic[ key ] ) )

def login( request ):
  return render_to_response( 'account/login.htm' );

def signin( request):
  checker = get_empty_val_checker( request.POST )
  if checker( 'name' ) and checker( 'pass' ):
    username = request.POST[ 'name' ]
    password = request.POST[ 'pass' ]
  else:
    return HttpResponseRedirect( \
      '/error/?msg=%s' % 'Both username and password cannot be empty' )

  if TalentUser.objects.filter( username__exact = username, \
    password__exact = hashlib.sha1( password ).hexdigest() )[:1]:
    return HttpResponseRedirect( '/search/' )
  else:
    return HttpResponseRedirect( \
      '/error/?msg=%s' % 'Invalid username or password' )

def signup( request ):
  checker = get_empty_val_checker( request.POST )
  if    checker( 'reg-name' ) and checker( 'reg-pass' ) \
    and checker( 'reg-title' ) and checker( 'reg-team' ):
    reg_name   = request.POST[ "reg-name"  ]
    reg_passwd = request.POST[ "reg-pass"  ]
    reg_title  = request.POST[ "reg-title" ]
    reg_team   = request.POST[ "reg-team"  ]
  else:
    return HttpResponseRedirect( \
      '/error/?msg=%s' % 'Invalid register data' )

  TalentUser( \
    username = reg_name, \
    password = hashlib.sha1( reg_passwd ).hexdigest(), \
    title    = reg_title,
    team     = reg_team ).save()
  return HttpResponseRedirect( '/search/' )

def signout( request ):
  return HttpResponseRedirect( '/' )
