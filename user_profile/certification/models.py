from django.db import models

# Create your models here.

class Certification( models.Model ):
  username    = models.CharField( max_length = 20 )
  cert_name   = models.CharField( max_length = 200 )
  cert_date   = models.DateTimeField( )


  def __unicode__( self ):
    return '[username: %s, certification: %s, date: %s]' %(self.username, self.cert_name, self.cert_date)


class CertificationManager:
  @staticmethod
  def find_cert_by_user( user ):
    return Certification.objects.filter( username = user )

  
  @staticmethod
  def store_cert_by_user( user, certname, certdate ):
    Certification.objects.filter( username__exact = user, cert_name__exact = certname ).delete()
    Certification( username = user, cert_name = certname, cert_date = certdate ).save()

