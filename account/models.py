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
