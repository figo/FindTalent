# Create your views here.
from django.shortcuts import render_to_response
from django.http      import HttpResponseRedirect

from FindTalent.common.models import SessionManager

def search( request ):
  ident = SessionManager( request.session ).check_cookie()

  if len( ident ) == 2:
    return render_to_response( 'search/index.htm', { 'username' : ident[ 0 ] } )
  else:
    return HttpResponseRedirect( '/' )
