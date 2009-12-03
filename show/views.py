# Create your views here.
from django.shortcuts import render_to_response
from django.http      import HttpResponseRedirect

from FindTalent.account.models import TalentUser
from FindTalent.common.models  import SessionManager

def show( request ):
  ident = SessionManager( request.session ).check_cookie()

  if len( ident ) == 2:
    user = TalentUser.objects.filter( username__exact = ident[ 0 ] )[:1].values()
    if len( user ) == 1:
      user = user[ 0 ]
      return render_to_response( 'show/index.htm', { 'username' : user['username'], 'title' : user['title'], 'team' : user['team'] } )
    else:
      return HttpResponseRedirect( '/error/?msg=Invalid cookie' )
  else:
    return HttpResponseRedirect( '/' )
