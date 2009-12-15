from FindTalent.account.models import TalentUser
from FindTalent.account.models import TalentGroup, GroupManager

import hashlib

password = hashlib.sha1( 'demo' ).hexdigest()

TalentUser( \
  username ='demo', \
  password = password, \
  title    = 'QA', \
  team     = 'SNAC', \
  picture  = 'http' ).save()
TalentUser( \
  username = 'Figo_Luo', \
  password = password, \
  title    = 'SQA', \
  team     = 'SNAC', \
  picture  = 'http').save()
TalentUser( \
  username = 'Tao_Wu', \
  password = password,\
  title    = 'SQA', \
  team     = 'SNAC', \
  picture  = 'http').save()
TalentUser( \
  username = 'Feng_Xiao', \
  password = password,\
  title    = 'SQA', \
  team     = 'SNAC', \
  picture  = 'http').save()

TalentGroup( \
  username  = 'demo', \
  groupname = 'basic' ).save()
TalentGroup( \
  username  = 'Figo_luo', \
  groupname = 'basic' ).save()
TalentGroup( \
  username  = 'Tao_Wu', \
  groupname = 'basic' ).save()
TalentGroup( \
  username  = 'Feng_Xiao', \
  groupname = 'basic' ).save()
GroupManager.add_user_to_group( 'demo', 'basic' )
