from FindTalent.account.models import TalentUser
from FindTalent.account.models import TalentGroup

import hashlib

password = hashlib.sha1( 'demo' ).hexdigest()

TalentUser( \
  username ='demo', \
  password = password, \
  title    = 'QA', \
  team     = 'SNAC', \
  picture  = 'http' ).save()
TalentUser( \
  username = 'lucy', \
  password = password, \
  title    = 'SE', \
  team     = 'SNAC', \
  picture  = 'http').save()
TalentUser( \
  username = 'abcdefghijk', \
  password = password ).save()
TalentUser( \
  username = 'q1w2e3r4', \
  password = password ).save()

TalentGroup( \
  username  = 'demo', \
  groupname = 'basic' ).save()
