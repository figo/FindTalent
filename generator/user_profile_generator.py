from FindTalent.user_profile.certification.models import Certification, CertificationManager
from FindTalent.user_profile.skill.models import Skill, SkillManager
from FindTalent.user_profile.project.models import Project, ProjectManager

CertificationManager.store_cert_by_user( 'demo', 'c++', '2009-12-02' )
SkillManager.store_skill_by_user( 'demo', 'c++', '5 years','senior' )
ProjectManager.store_project_by_user( 'demo', 'Jasper', '2009-12-02','2010-03-02','vc', 'dell 3400','wireshark','run cases')

