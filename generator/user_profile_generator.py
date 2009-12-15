from FindTalent.user_profile.certification.models import Certification, CertificationManager
from FindTalent.user_profile.skill.models import Skill, SkillManager
from FindTalent.user_profile.project.models import Project, ProjectManager

CertificationManager.store_cert_by_user( 'demo', 'CCNE', '2009-12-02' )
SkillManager.store_skill_by_user( 'demo', 'c', '5 years','senior' )
SkillManager.store_skill_by_user( 'demo', 'java', '5 years','senior' )
SkillManager.store_skill_by_user( 'demo', 'perl', '5 years','senior' )
ProjectManager.store_project_by_user( 'demo', 'Jasper', '2009-12-02','2010-03-02','vc', 'dell 3400','wireshark','run cases')

CertificationManager.store_cert_by_user( 'Figo_Luo', 'CCNE', '2009-12-02' )
SkillManager.store_skill_by_user( 'Figo_Luo', 'c++', '5 years','senior' )
SkillManager.store_skill_by_user( 'Figo_Luo', 'java', '5 years','senior' )
SkillManager.store_skill_by_user( 'Figo_Luo', 'perl', '5 years','senior' )
ProjectManager.store_project_by_user( 'Figo_Luo', 'Jasper', '2009-12-02','2010-03-02','vc', 'dell 3400','wireshark','run cases')

CertificationManager.store_cert_by_user( 'Tao_Wu', 'CCNE', '2009-12-02' )
SkillManager.store_skill_by_user( 'Tao_Wu', 'c', '5 years','senior' )
SkillManager.store_skill_by_user( 'Tao_Wu', 'PHP', '5 years','senior' )
SkillManager.store_skill_by_user( 'Tao_Wu', 'perl', '5 years','senior' )
ProjectManager.store_project_by_user( 'Tao_Wu', 'Jade', '2009-12-02','2010-03-02','vc', 'dell 3400','wireshark','run cases')

CertificationManager.store_cert_by_user( 'Feng_Xiao', 'CCNE', '2009-12-02' )
SkillManager.store_skill_by_user( 'Feng_Xiao', 'c', '5 years','senior' )
SkillManager.store_skill_by_user( 'Feng_Xiao', 'java', '5 years','senior' )
SkillManager.store_skill_by_user( 'Feng_Xiao', 'perl', '5 years','senior' )
ProjectManager.store_project_by_user( 'Feng_Xiao', 'Ruby', '2009-12-02','2010-03-02','vc', 'dell 3400','wireshark','run cases')

