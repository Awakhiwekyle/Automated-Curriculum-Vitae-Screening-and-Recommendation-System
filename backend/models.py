from app import db, ma
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=True, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=True, unique=False)    
    created = db.Column(db.String(50), nullable=False)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    surname = db.Column(db.String(50), nullable=False, unique=False)
    mobile = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=False, unique=False)    
    country = db.Column(db.String(50), nullable=False, unique=False)    
    created = db.Column(db.String(50), nullable=False)

class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobtitle = db.Column(db.String(50), nullable=False, unique=False)
    company = db.Column(db.String(50), nullable=False, unique=False)
    city = db.Column(db.String(50), nullable=False, unique=False)
    currently = db.Column(db.String(50), nullable=False, unique=False)
    years = db.Column(db.String(50), nullable=False)
    months = db.Column(db.String(50), nullable=False, unique=False)    
    description = db.Column(db.String(200), nullable=False, unique=False)    
    username = db.Column(db.String(50), nullable=False, unique=False)
    created = db.Column(db.String(50), nullable=False, unique=False)

class ExperienceSchema(ma.ModelSchema):
    class Meta:
        model = Experience

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(50), nullable=False, unique=False)
    school = db.Column(db.String(50), nullable=False, unique=False)
    city = db.Column(db.String(50), nullable=False, unique=False)
    fieldOfStudy = db.Column(db.String(50), nullable=False, unique=False)
    duration = db.Column(db.String(50), nullable=False)       
    username = db.Column(db.String(50), nullable=False, unique=False)
    created = db.Column(db.String(50), nullable=False, unique=False)

class EducationSchema(ma.ModelSchema):
    class Meta:
        model = Education

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(200), nullable=False, unique=False)    
    experience = db.Column(db.String(200), nullable=False)       
    username = db.Column(db.String(50), nullable=False, unique=False)
    created = db.Column(db.String(50), nullable=False, unique=False)

class SkillsSchema(ma.ModelSchema):
    class Meta:
        model = Skills

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    company_name = db.Column(db.String(50), nullable=False, unique=False)    
    created = db.Column(db.String(50), nullable=False)    

class EmployerSchema(ma.ModelSchema):
    class Meta:
        model = Employer

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    company = db.Column(db.String(50), nullable=False, unique=False)
    job_title = db.Column(db.String(50), nullable=False, unique=False)    
    experience_needed = db.Column(db.String(50), nullable=False)       
    skills_needed = db.Column(db.String(100), nullable=False, unique=False)
    education_needed = db.Column(db.String(100), nullable=False, unique=False)
    ad_starts = db.Column(db.Date, nullable=False, unique=False)
    ad_ends = db.Column(db.Date, nullable=False, unique=False)
    city = db.Column(db.String(50), nullable=False, unique=False)    
    country = db.Column(db.String(50), nullable=False, unique=False)
    created = db.Column(db.Date, nullable=False, unique=False)
    employer_email = db.Column(db.String(50), nullable=False, unique=True)

class JobSchema(ma.ModelSchema):
    class Meta:
        model = Job

class Applications(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    job_id = db.Column(db.Integer)    
    applicant_id = db.Column(db.Integer)
    application_score = db.Column(db.Float)   
    created = db.Column(db.String(50), nullable=False, unique=False)
   

class ApplicationsSchema(ma.ModelSchema):
    class Meta:
        model = Applications