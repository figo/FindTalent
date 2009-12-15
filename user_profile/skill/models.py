from django.db import models
from FindTalent.account.models import TalentUser

# Create your models here.

class Skill( models.Model ):
  username    = models.ForeignKey( TalentUser )
  skill       = models.CharField( max_length = 50 )
  experience  = models.CharField( max_length = 30 )
  level       = models.CharField( max_length = 30 )


  def __unicode__( self ):
    return '[ skill: %s, experience: %s, level: %s]' %(self.skill, self.experience, self.level)


class SkillTest( models.Model ):
  name = models.ForeignKey( TalentUser )
  test = models.CharField(max_length =20)


class SkillManager:
  @staticmethod
  def find_skill_by_user( user ):
    return Skill.objects.filter( username = TalentUser.objects.get(username=user))

  
  @staticmethod
  def store_skill_by_user(user, skill, experience, level ):
    Skill.objects.filter( \
      username__exact = TalentUser.objects.get(username=user),\
      skill__exact = skill ).delete()
    Skill( \
      username = TalentUser.objects.get(username=user), \
      skill = skill, \
      experience = experience, \
      level = level ).save()
 
