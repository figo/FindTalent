from django.db import models

# Create your models here.

class Skill( models.Model ):
  username    = models.CharField( max_length = 20 )
  skill       = models.CharField( max_length = 50 )
  experience  = models.CharField( max_length = 30 )
  level       = models.CharField( max_length = 30 )


  def __unicode__( self ):
    return '[username: %s, skill: %s, experience: %s, level: %s]' %(self.username, self.skill, self.experience, self.level)


class SkillManager:
  @staticmethod
  def find_skill_by_user( user ):
    return Skill.objects.filter( username = user )

  
  @staticmethod
  def store_skill_by_user(user, skill, experience, level ):
    Skill.objects.filter( \
      username__exact = user,\
      skill__exact = skill ).delete()
    Skill( \
      username = user, \
      skill = skill, \
      experience = experience, \
      level = level ).save()
 
