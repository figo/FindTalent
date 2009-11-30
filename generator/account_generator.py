from FindTalent.account.models import TalentUsers
import base64
import hashlib

pass_hash = hashlib.md5()
pass_hash.update('654123')
hash_value = pass_hash.digest()
value = base64.encodestring(hash_value)

TalentUsers(username='lily', password=value, title='QA',team='SNAC',picture='http').save()
TalentUsers(username='lucy', password=value,title='SE',team='SNAC',picture='http').save()
TalentUsers(username='abcdefghijk', password=value).save()
TalentUsers(username='q1w2e3r4', password=value).save()
