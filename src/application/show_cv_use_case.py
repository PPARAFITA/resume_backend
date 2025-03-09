from src.core.interfaces import (
user_service_interf,
education_service_interf,
work_experience_service_interf )
from src.core.schemas import UserBase, User, CV, WorkExperienceSchema, EducationSchema


class ShowCV():
    def __init__( self, education_service: education_service_interf, user_service: user_service_interf, work_experience_service: work_experience_service_interf ):
        self.education_service = education_service
        self.user_service = user_service
        self.work_experience_service = work_experience_service

    def get_resume_cv(self, userid: int) -> CV:
        education_data = self.education_service.get_educations_by_user(userid)  
        personalInfo_data = self.user_service.get_user_by_id(userid)
        work_experience_data = self.work_experience_service.get_works_by_user(userid) 

         # Convertimos los datos de los servicios a los esquemas correspondientes
        education_list = [EducationSchema(**edu.__dict__) for edu in education_data]
        work_experience_list = [WorkExperienceSchema(**work.__dict__) for work in work_experience_data]  
        personal_info = personalInfo_data
        
        cv = CV(
            **personal_info.dict(),  
            work_experience=work_experience_list,
            education=education_list
        )
        
        return cv