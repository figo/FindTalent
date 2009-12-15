from django.db import models
from FindTalent.account.models import TalentUser
# Create your models here.

class Certification( models.Model ):
  username    = models.ForeignKey( TalentUser )
  cert_name   = models.CharField( max_length = 200 )
  cert_date   = models.DateTimeField( )


  def __unicode__( self ):
    return '[certification: %s, date: %s]' %(self.cert_name, self.cert_date)


class CertificationManager:
  @staticmethod
  def find_cert_by_user( user ):
    return Certification.objects.filter( username = TalentUser.objects.get(username = user) )

  
  @staticmethod
  def store_cert_by_user( user, certname, certdate ):
    Certification.objects.filter( username__exact = TalentUser.objects.get(username=user), cert_name__exact = certname ).delete()
    Certification( username = TalentUser.objects.get(username=user), cert_name = certname, cert_date = certdate ).save()

