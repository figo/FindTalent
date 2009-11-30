# Create your views here.
from django.shortcuts import render_to_response

def error( request ):
  if request.GET.has_key( 'msg' ) and request.GET[ 'msg' ]:
    return render_to_response( 'common/error.htm', { 'msg' : request.GET[ 'msg'] } )
  else:
    return render_to_response( 'common/error.htm' )
