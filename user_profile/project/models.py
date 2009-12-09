from django.db import models

# Create your models here.

class Project( models.Model ):
  username       = models.CharField( max_length = 20 )
  description    = models.CharField( max_length = 200 )
  start_time     = models.DateTimeField( )
  end_time       = models.DateTimeField( )
  tools          = models.CharField( max_length = 500 )
  hardware       = models.CharField( max_length = 500 )
  software       = models.CharField( max_length = 500 )
  respon         = models.CharField( max_length = 500 )


  def __unicode__( self ):
    return '[username: %s, decription: %s, start from: %s, end: %s, tools used: %s, hardware: %s, software: %s, responsibility]' %(self.username, self.description, self.start_time, self.end_time, self.tools,self.hardware_enviro, self.software_enviro, self.reponsibility)


class ProjectManager:
  @staticmethod
  def find_project_by_user( user ):
    return Project.objects.filter( username = user )

  
  @staticmethod
  def store_project_by_user(user, description, start, end, tools, hardware, software, respon ):
    Project.objects.filter( \
       username__exact = user,\
       description__exact = description ).delete()
    Project( \
      username = user, \
      description = description,\
      start_time =  start,\
      end_time   =  end,\
      tools      =  tools,\
      hardware   =  hardware,\
      software   =  software,\
      respon     =  respon ).save()


