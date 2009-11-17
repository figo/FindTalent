# Create your views here.
from django.shortcuts import render_to_response

def show( request ):
  return render_to_response( 'show/index.htm' );
