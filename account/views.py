# Create your views here.
from django.shortcuts import render_to_response
from FindTalent.account.models import TalentUsers
import base64
import hashlib

def login( request ):
  return render_to_response( 'account/login.htm' );



def signin( request):

  user = request.POST[ "name" ]
  password = request.POST[ "pass" ]
  if len(user) == 0 or len(password) == 0:
    return render_to_response( 'account/login.htm' )

  hash = hashlib.md5()
  hash.update(password) 
  pass_hash = hash.digest()
  base64_pass_hash = base64.encodestring(pass_hash)

  all_entry_list = list(TalentUsers.objects.filter(username = user).filter(password = base64_pass_hash))

  if len(all_entry_list) == 0:
    return render_to_response( 'account/login.htm' )

  return render_to_response( 'search/index.htm' )



def signup( request ):
  
  reg_name = request.POST[ "reg-name" ]
  reg_passd = request.POST["reg-pass"]
  reg_passd_again = request.POST["reg-pass-again"]
  reg_title = request.POST["reg-title"]
  reg_team = request.POST["reg-team"]
  
  if len(reg_name) == 0 or  len(reg_passd) == 0 or len(reg_passd_again) == 0 or len(reg_title) == 0 or len(reg_team) == 0 or reg_passd != reg_passd_again:
    return render_to_response( 'account/login.htm' )


  hash = hashlib.md5()
  hash.update(reg_passd) 
  pass_hash = hash.digest()
  base64_pass_hash = base64.encodestring(pass_hash)
  
  TalentUsers(username = reg_name, password = base64_pass_hash, title = reg_title, team = reg_team).save()
  return render_to_response( 'search/index.htm' )

def signout( request ):
  return render_to_response( 'account/login.htm' )
