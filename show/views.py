# Create your views here.
from django.shortcuts import render_to_response
from django.http      import HttpResponseRedirect

from FindTalent.account.models import TalentUser
from FindTalent.common.models  import SessionManager

def show( request ):
  ident = SessionManager( request.session ).check_cookie()

  if len( ident ) == 2:
    if request.GET.has_key( 'name' ) and request.GET[ 'name' ]:
      username = request.GET[ 'name' ]
    else:
      username = ident[ 0 ]

    user = TalentUser.objects.filter( username__exact = username )[:1].values()
    if len( user ) == 1:
      user = user[ 0 ]
      return render_to_response( 'show/index.htm', { 'username' : ident[ 0 ], 'showuser' : user[ 'username' ], 'title' : user[ 'title' ], 'team' : user[ 'team' ] } )
    else:
      return HttpResponseRedirect( \
        '/error/?msg=Cannot find user: [%s]' % username )
  else:
    return HttpResponseRedirect( '/' )
