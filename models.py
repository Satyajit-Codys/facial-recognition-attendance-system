from app import db

class Student(db.Model):
    __tablename__ = 'Student'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(80))
    semester = db.Column(db.String(80))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))
    pic_path = db.Column(db.Text)
    registered_on = db.Column(db.DateTime)

class Faculty(db.Model):
    __tablename__ = 'Faculty'
    __table_args__ = {'extend_existing': True}

    f_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    course_id = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))
    is_admin = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime)

class Attendance(db.Model):
    __tablename__ = 'Attendance'
    __table_args__ = {'extend_existing': True}

    att_id = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    lecture_no = db.Column(db.Integer)
    marked_by = db.Column(db.String(80))
    marked_date = db.Column(db.Date)
    marked_time = db.Column(db.Time)

class Course(db.Model):
    __tablename__ = 'Course'
    __table_args__ = {'extend_existing': True}

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80))
    total_lectures = db.Column(db.Integer)
    teacher_email = db.Column(db.String(800))
    students_email=  db.Column(db.String(500))
    

db.create_all()
