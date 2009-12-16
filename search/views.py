# Create your views here.
from django.shortcuts import render_to_response
from django.http      import HttpResponseRedirect
from FindTalent.common.models import TalentHelper,SessionManager
from FindTalent.user_profile.skill.models import Skill
from FindTalent.user_profile.project.models import Project
from FindTalent.user_profile.certification.models import Certification
from FindTalent.account.models import TalentUser

def search( request ):
  ident = SessionManager( request.session ).check_cookie()

  if len( ident ) != 2:
    return HttpResponseRedirect( '/' )
 
  checker = TalentHelper.get_empty_val_checker( request.GET )
  if not checker( 'type' ) or not checker ( 'key' ):
       result = TalentUser.objects.all()
       return render_to_response( 'search/index.htm', { 'all_search_result' : result, 'total_qualified':len(result) } )
  
  else:
       search_type = request.GET[ 'type' ]
       search_key  = request.GET[ 'key' ]
       
       if ( search_type == 'project' ):
         result = Project.objects.filter( description__icontains=search_key )
       if ( search_type == 'skill' ):
         result = Skill.objects.filter( skill__icontains=search_key )
       if ( search_type == 'certification' ):
         result = Certification.objects.filter( cert_name__icontains=search_key )
       
       users = []
       for re in result:
         users.append(re.username)
       
       return render_to_response( 'search/index.htm', { 'all_search_result' : users, 'total_qualified':len(users) } )
