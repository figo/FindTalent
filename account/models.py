from django.db import models

# Create your models here.
class TalentUser( models.Model ):
  username = models.CharField( max_length = 20 )
  password = models.CharField( max_length = 40 )
  title    = models.CharField( max_length = 50 )
  team     = models.CharField( max_length = 50 )
  picture  = models.FileField( upload_to  = '/static/upload' )
  reg_time = models.DateTimeField( auto_now_add = True )

  def __unicode__( self ):
    return '[Username: %s, Password: %s, Title: %s, Team: %s, Pics: %s]' % ( self.username, self.password, self.title, self.team, self.picture )

class TalentGroup( models.Model ):
  username  = models.CharField( max_length = 20 )
  groupname = models.CharField( max_length = 50 )

  def __unicode__( self ):
    return '[Username: %s, Groupname: %s]' % ( self.username, self.groupname )

class GroupManager:
  @staticmethod
  def add_user_to_group( user, group ):
    TalentGroup( username = user, groupname = group ).save()

  def del_user_from_group( user, group ):
    TalentGroup.objects.filter( \
      username__exact  = user, \
      groupname__exact = group ).delete()

  @staticmethod
  def is_user_in_group( user, group ):
    return TalentGroup.objects.filter( \
      username__exact  = user, \
      groupname__exact = group )[:1]
