# Create your views here.
from django.shortcuts import render_to_response
from django.http      import HttpResponseRedirect
from django.conf      import settings
from datetime         import datetime
import hashlib, os

from FindTalent.common.models  import TalentHelper, SessionManager
from FindTalent.account.models import TalentUser

def index( request ):
  return render_to_response( 'account/index.htm' );

def signin( request):
  checker = TalentHelper.get_empty_val_checker( request.POST )
  if checker( 'name' ) and checker( 'pass' ):
    username = request.POST[ 'name' ]
    password = request.POST[ 'pass' ]
  else:
    return HttpResponseRedirect( \
      '/error/?msg=%s' % 'Both username and password cannot be empty' )

  if TalentUser.objects.filter( username__exact = username, \
    password__exact = hashlib.sha1( password ).hexdigest() )[:1]:
    SessionManager( request.session ).set_cookie( username )
    return HttpResponseRedirect( '/search/' )
  else:
    return HttpResponseRedirect( \
      '/error/?msg=%s' % 'Invalid username or password' )

def signup( request ):
  checker = TalentHelper.get_empty_val_checker( request.POST )
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
  SessionManager( request.session ).set_cookie( reg_name )
  return HttpResponseRedirect( '/search/' )

def signout( request ):
  SessionManager( request.session ).clr_cookie()
  return HttpResponseRedirect( '/' )

def uploadimg( request ):
  if not request.FILES.has_key( 'Filedata' ):
    return render_to_response( 'account/upload_img.json', { 'result' : 'FAIL' } )

  ext = os.path.splitext( request.FILES[ 'Filedata' ].name )[ 1 ]
  if ext in ( '.jpg', '.png', '.gif' ):
    filename =  datetime.now().strftime( '%Y%m%d%H%M%S' )
    filename += ext

    file = open( settings.UPLOAD_IMG_ROOT + '/' + filename, 'wb+' )
    for chunk in request.FILES[ 'Filedata' ].chunks():
      file.write( chunk )
    file.close()

    return render_to_response( 'account/upload_img.json', \
      { 'result' : 'PASS', 'filename' : filename } )
  else:
    return render_to_response( 'account/upload_img.json', { 'result' : 'FAIL' } )
