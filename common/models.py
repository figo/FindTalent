from django.db import models
from datetime  import datetime

# Create your models here.
class TalentHelper:
  @staticmethod
  def get_empty_val_checker( dic ):
    return ( lambda key: ( dic.has_key( key ) and dic[ key ] ) )

class SessionManager:
  def __init__( self, session ):
    self.session  = session

  def set_cookie( self, username ):
    self.session[ 'username'  ] = username
    self.session[ 'logintime' ] = datetime.now()

  def check_cookie( self ):
    if self.session.has_key( 'username' ) and self.session.has_key( 'logintime' ):
      return ( self.session[ 'username' ], self.session[ 'logintime' ] )
    else:
      return ()

  def clr_cookie( self ):
    self.session.clear()
