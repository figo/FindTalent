from django.db import models

# Create your models here.
class TalentUsers(models.Model):
  username    = models.CharField( max_length = 20 )
  password    = models.CharField( max_length = 40 )
  title       = models.CharField( max_length = 50 )
  team        = models.CharField( max_length = 50 )
  picture     = models.FileField( upload_to='/static/upload' )

  def __unicode__(self):
    return '(%s, %s, %s, %s)' % ( self.username, self.password, self.title, self.team, self.picture )
