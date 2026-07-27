from dataclasses import dataclass
from pathlib import Path

@dataclass
class ProfileConfig:
    sam_profile_image:str = f"{Path(__file__).resolve().parent}/assets/img/linkedin_pic.jpg"
    github_profile:str = 'https://github.com/ayodelephillips'
    linkedin_profile:str ='https://www.linkedin.com/in/samuel-phillips-dev'
    resume_location:str = f"{Path(__file__).resolve().parent}/assets/file/samuel_phillips_resume.docx"
    resume_file_name:str = "samuel_phillips_resume.docx"
    gcp_certification_url:str = "https://www.credly.com/badges/4a96d66e-1411-498c-99c0-05b189633fe1/public_url"