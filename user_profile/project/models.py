from django.db import models
from FindTalent.account.models import TalentUser

# Create your models here.

class Project( models.Model ):
  username       = models.ForeignKey( TalentUser )
  description    = models.CharField( max_length = 200 )
  start_time     = models.DateTimeField( )
  end_time       = models.DateTimeField( )
  tools          = models.CharField( max_length = 500 )
  hardware       = models.CharField( max_length = 500 )
  software       = models.CharField( max_length = 500 )
  respon         = models.CharField( max_length = 500 )


  def __unicode__( self ):
    return '[ decription: %s, tools used: %s, hardware: %s, software: %s, responsibility:%s]' %(self.description,self.tools,self.hardware, self.software, self.respon)


class ProjectManager:
  @staticmethod
  def find_project_by_user( user ):
    return Project.objects.filter( username = TalentUser.objects.get(username=user) )

  
  @staticmethod
  def store_project_by_user(user, description, start, end, tools, hardware, software, respon ):
    Project.objects.filter( \
       username__exact = TalentUser.objects.get(username=user),\
       description__exact = description ).delete()
    Project( \
      username = TalentUser.objects.get(username=user), \
      description = description,\
      start_time =  start,\
      end_time   =  end,\
      tools      =  tools,\
      hardware   =  hardware,\
      software   =  software,\
      respon     =  respon ).save()


