from app import *
import pdb
from sqlalchemy.exc import IntegrityError
from parse import *
# from models import *
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user, login_user,logout_user


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('adminlogin'))
        
administrator = Admin(app, index_view = MyAdminIndexView())
administrator.add_view(MyModelView(Users, db.session))
administrator.add_view(MyModelView(Person, db.session))
administrator.add_view(MyModelView(Experience, db.session))
administrator.add_view(MyModelView(Education, db.session))
administrator.add_view(MyModelView(Skills, db.session))
administrator.add_view(MyModelView(Employer, db.session))
administrator.add_view(MyModelView(Job, db.session))
administrator.add_view(MyModelView(Applications, db.session))

login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

#admin login

@app.route('/adminlogin')
def adminlogin():
    user = Users.query.get(2)
    login_user(user)
    return 'Logged in'

@app.route('/adminlogout')
def adminlogout():
    logout_user()
    return 'Logged Out'

# logout
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    g.user = None
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:        
        g.user = session['user']
        g.id = session['id']
        g.role = session['role']
        g.empId = session['empId']
        print(g.user)
        load_notifications() 

# receives login details
@app.route('/login', methods=['POST'])
def login():    
    if request.method == 'POST':
        i = request.get_json()
        username = i["username"]
        password = i["password"]
        try: 
            # pdb.set_trace()           
            user = Users.query.filter_by(username = username).filter_by(password=password).first() 
        except Exception as e:
            return json.dumps({"error":"Database failure"}) 
        if username == '' or password == '':
            return json.dumps({"error":"Enter all credentials"})      
        elif user is None:
            return json.dumps({"error":"Incorrect credentials"})
        else:            
            person = {}
            # person["fullname"] = user.fullname            
            person["username"] = user.username  
            # person["role"] = user.role
            session["user"] = user.id             
            return json.dumps({"payload": person})

    else:
        return json.dumps({'error':'Log in first'})
    
# post new users
@app.route('/newUser', methods=['POST'])
@cross_origin()
def newUser():    
    if request.method == 'POST':
        i = request.get_json()       
        user = Users()        
        user.email = i["email"]
        user.username = i["username"]               
        user.password = i["password"]
        user.created = datetime.datetime.now()
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            dupe_field = parse('(1062, "Duplicate entry \'{}\' for key \'{}\'")', str(e.orig))
            if(dupe_field[1] == 'email'):
                return jsonify({"error": "Email already registered in system"})
            elif(dupe_field[1] == 'username'):
                return jsonify({"error": "Username already taken"})

        except Exception as f:
            cantConnet = parse('({}, "Can\'t connect to MySQL server on \'localhost\' (10061)")', str(f.orig))
            if(cantConnet):
                if(cantConnet[0] == '2003'):
                    return jsonify({"error": "Cannot connect to system database"})

        except Exception as g:
            goneAway = parse('({}, "MySQL server has gone away")', str(g.orig))
            if(goneAway):
                if(goneAway[0] == '2006'):
                    return jsonify({"error": "System database off "})

        except Exception as h:
            return jsonify({"error": str(h)})
        
        return jsonify({"success":"successfully added user"})

# post new person
@app.route('/newPerson', methods=['POST'])
@cross_origin()
def newPerson():    
    if request.method == 'POST':
        i = request.get_json()       
        person = Person() 
        person.name = i["name"]
        person.surname = i["surname"]
        person.mobile = i["mobile"]        
        person.email = i["email"]        
        person.city = i["city"] 
        person.country = i["country"] 
        person.username = i["username"] 
        person.created = datetime.datetime.now()
        try:
            db.session.add(person)
            db.session.commit()
        except IntegrityError as e:
            dupe_field = parse('(1062, "Duplicate entry \'{}\' for key \'{}\'")', str(e.orig))
            if(dupe_field[1] == 'email'):
                return jsonify({"error": "Email already registered in system"})
            elif(dupe_field[1] == 'username'):
                return jsonify({"error": "Username already taken"})

        except Exception as f:
            cantConnet = parse('({}, "Can\'t connect to MySQL server on \'localhost\' (10061)")', str(f.orig))
            if(cantConnet):
                if(cantConnet[0] == '2003'):
                    return jsonify({"error": "Cannot connect to system database"})

        except Exception as g:
            goneAway = parse('({}, "MySQL server has gone away")', str(g.orig))
            if(goneAway):
                if(goneAway[0] == '2006'):
                    return jsonify({"error": "System database off "})

        except Exception as h:
            return jsonify({"error": str(h)})
        
        return jsonify({"success":"successfully added person"})

# Get person 
@app.route('/getPerson/<username>', methods=['GET'])
def getPerson(username):
    person_schema = PersonSchema()
    try:
        person = Person.query.filter_by(username = username).first() 
        # pdb.set_trace()
        if request.method == 'GET':            
            # return jsonify({"person": person})
            x = person_schema.dump(person)
            # pdb.set_trace()
            return jsonify(x)
    except Exception as e:
        return jsonify({"error": str(e)})

# update person
@app.route('/updatePerson', methods=['PATCH'])
def updatePerson():
    i = request.get_json()
    person = db.session.query(Person).filter_by(username = i["username"]).first()      
    person.name = i["name"]
    person.surname = i["surname"]
    person.mobile = i["mobile"]        
    person.email = i["email"]        
    person.city = i["city"] 
    person.country = i["country"] 
    person.username = i["username"]    
    person.created = datetime.datetime.now()
    # pdb.set_trace() 
    try:        
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"success":"success"})

# post new experience
@app.route('/newExperience', methods=['POST'])
@cross_origin()
def newExperience():    
    if request.method == 'POST':
        i = request.get_json()       
        experience = Experience() 
        experience.jobtitle = i["jobtitle"]
        experience.company = i["company"]
        experience.city = i["city"]        
        experience.currently = i["currently"] 
        experience.years = i["years"] 
        experience.months = i["months"] 
        experience.username = i["username"] 
        experience.description = i["description"] 
        experience.created = datetime.datetime.now()
        # pdb.set_trace()
        try:
            db.session.add(experience)
            db.session.commit()
        
        except Exception as h:
            return jsonify({"error": str(h)})
        
        return jsonify({"success":"successfully added person"})

@app.route('/getExperience/<username>', methods=['GET'])
def getExperience(username):    
    experience_schema = ExperienceSchema(many=True)
    try:
        experience = Experience.query.filter_by(username = username).all()
        if request.method == 'GET':
            x = experience_schema.dump(experience)            
            return jsonify(x)
    except Exception as e:
        return jsonify({"error": str(e)})

# delete experience
@app.route('/deleteExperience/<id>', methods=['GET'])
def deleteExperience(id):
    exp = Experience.query.filter_by(id = id).first() 
    try:   
        db.session.delete(exp)     
        db.session.commit()
    except Exception as e:
        return jsonify({"error": "Error deleting experience"})

    return jsonify({"success":"successfully deleted experience"})

# update experience
@app.route('/updateExperience', methods=['PATCH'])
def updateExperience():
    i = request.get_json()
    experience = db.session.query(Experience).filter_by(username = i["username"]).first()      
    experience = Experience() 
    experience.jobtitle = i["jobtitle"]
    experience.company = i["company"]
    experience.city = i["city"]        
    experience.currently = i["currently"] 
    experience.years = i["years"] 
    experience.months = i["months"] 
    experience.username = i["username"] 
    experience.description = i["description"] 
    experience.created = datetime.datetime.now()
    # pdb.set_trace() 
    try:        
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"success":"success"})

# post new Education
@app.route('/newEducation', methods=['POST'])
@cross_origin()
def newEducation():    
    if request.method == 'POST':
        i = request.get_json()       
        education = Education() 
        education.degree = i["degree"]
        education.school = i["school"]
        education.city = i["city"]        
        education.duration = i["duration"] 
        education.fieldOfStudy = i["fieldOfStudy"]         
        education.username = i["username"] 
        education.created = datetime.datetime.now()
        # pdb.set_trace()
        try:
            db.session.add(education)
            db.session.commit()
        
        except Exception as h:
            return jsonify({"error": str(h)})
        
        return jsonify({"success":"successfully added person"})

#get Education
@app.route('/getEducation/<username>', methods=['GET'])
def getEducation(username):    
    education_schema = EducationSchema(many=True)
    try:
        education = Education.query.filter_by(username = username).all()
        if request.method == 'GET':
            x = education_schema.dump(education)            
            return jsonify(x)
    except Exception as e:
        return jsonify({"error": str(e)})

# delete education
@app.route('/deleteEducation/<id>', methods=['GET'])
def deleteEducation(id):
    edu = Education.query.filter_by(id = id).first() 
    try:   
        db.session.delete(edu)     
        db.session.commit()
    except Exception as e:
        return jsonify({"error": "Error deleting education"})

    return jsonify({"success":"successfully deleted education"})

# update education
@app.route('/updateEducation', methods=['PATCH'])
def updateEducation():
    i = request.get_json()
    education = db.session.query(Education).filter_by(username = i["username"]).first()      
    education = Education() 
    education.degree = i["degree"]
    education.school = i["school"]
    education.city = i["city"]        
    education.duration = i["duration"] 
    education.fieldOfStudy = i["fieldOfStudy"]         
    education.username = i["username"] 
    education.created = datetime.datetime.now()
    try:        
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"success":"success"})

# post new skill
@app.route('/newSkill', methods=['POST'])
@cross_origin()
def newSkill():    
    if request.method == 'POST':
        i = request.get_json()       
        skills = Skills() 
        skills.skill = i["skill"]
        skills.experience = i["experience"]        
        skills.username = i["username"] 
        skills.created = datetime.datetime.now()
        # pdb.set_trace()
        try:
            db.session.add(skills)
            db.session.commit()
        
        except Exception as h:
            return jsonify({"error": str(h)})
        
        return jsonify({"success":"successfully added person"})

#get Skills
@app.route('/getSkills/<username>', methods=['GET'])
def getSkills(username):    
    skills_schema = SkillsSchema(many=True)
    try:
        skills = Skills.query.filter_by(username = username).all()
        if request.method == 'GET':
            x = skills_schema.dump(skills)            
            return jsonify(x)
    except Exception as e:
        return jsonify({"error": str(e)})

# delete Skill
@app.route('/deleteSkills/<id>', methods=['GET'])
def deleteSkills(id):
    skill = Education.query.filter_by(id = id).first() 
    try:   
        db.session.delete(skill)     
        db.session.commit()
    except Exception as e:
        return jsonify({"error": "Error deleting education"})

    return jsonify({"success":"successfully deleted education"})

# update Skills
@app.route('/updateSkill', methods=['PATCH'])
def updateSkill():
    i = request.get_json()
    skills_ = db.session.query(Skills).filter_by(username = i["username"]).first()
    skills = Skills()    
    skills.skill = i["skill"]
    skills.experience = i["experience"]
    skills.username = i["username"] 
    skills.created = datetime.datetime.now()
    try:        
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"success":"success"})


#get Jobs
@app.route('/getJobs/<username>', methods=['GET'])
def getJobs(username):    
    jobs_schema = JobSchema(many=True)
    try:
        # jobs = Job.query.all()
        applicant = Users.query.filter_by(username = username).first()
        applicant_id = applicant.id
        # pdb.set_trace()
        #jobs = db.session.query(Job).filter(~exists().where(Applications.job_id == Job.id )).all()
        #jobs = db.session.query(Job).join.filter(applicant_id).all() 
        #jobs = db.session.query(Job,Applications,Users).filter(Job.id == Applications.job_id).filter(Applications.applicant_id == Users.id).filter(Users.id != applicant_id).all()
        # pdb.set_trace()       
        jobs = db.session.query(Job).all()       
        if request.method == 'GET':            
            y = []            
            for job in jobs:
                x = {}
                x["id"] = job.id
                x["company"] = job.company
                x["experience_needed"] = job.experience_needed
                x["skills_needed"] = job.skills_needed
                x["education_needed"] = job.education_needed
                x["ad_starts"] = job.ad_starts
                x["ad_ends"] = job.ad_ends
                x["city"] = job.city
                x["country"] = job.country
                # pdb.set_trace()            
                y.append(x)
            
            return json.dumps(y)
    except Exception as e:
        return jsonify({"error": str(e)})


# post new application
@app.route('/postApplication', methods=['POST'])
@cross_origin()
def postApplication():    
    if request.method == 'POST':        
        i = request.get_json()
        # pdb.set_trace()       
        application = Applications()        
        application.job_id = i["job_id"]
        x = Users.query.filter_by(username = i["username"]).first()               
        application.applicant_id = str(x.id)        
        application.application_score = application_score_calc(i["username"], i["job_id"])
        application.created = datetime.datetime.now()
        # pdb.set_trace()
        try:
            db.session.add(application)
            db.session.commit()
        
        except Exception as h:
            return jsonify({"error": str(h)})
        
        return jsonify({"success":"success"})

def application_score_calc(username, job_id):
    import jieba
    import gensim
    from gensim import corpora    
    skills = Skills.query.filter_by(username = username).first()
    # pdb.set_trace()
    skills = skills.skill
    education = Education.query.filter_by(username = username).first()
    education = education.degree + ", " + education.fieldOfStudy
    experience = Experience.query.filter_by(username = username).first()
    experience = experience.jobtitle + ", " + experience.description 
    texts = [skills, education, experience]
    texts = [jieba.lcut(text) for text in texts]
    dictionary = corpora.Dictionary(texts)
    # print("dictionary is starts")
    # print(dictionary.token2id)
    # print("dictionary is ends")
    # Use [Dictionary] to convert [search word] to [sparse vector]
    keyword = Job.query.filter_by(id = job_id).first()
    keyword = keyword.job_title + keyword.experience_needed + keyword.skills_needed + keyword.education_needed
    kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
    # print("Key word starts")
    # print(keyword)
    # print("Key word ends")
    feature_cnt = len(dictionary.token2id)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = gensim.models.TfidfModel(corpus)
    index = gensim.similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = feature_cnt)    
    sim = index[tfidf[kw_vector]]
    print('Skill:' + str(sim[0]))
    print('Education:' + str(sim[1]))
    print('Experience:' + str(sim[2]))
    return sim[0] + sim[1] + sim[2]