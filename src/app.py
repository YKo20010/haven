import json
from db import db, Course, User, Assignment
from flask import Flask, request
from datetime import datetime

db_filename = "todo.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# Get all courses
# GET /api/courses/
@app.route('/')
@app.route('/api/courses/')
def get_courses():
    courses = Course.query.all()
    res = {'success': True, 'data': [c.serialize() for c in courses]}
    return json.dumps(res), 200

# Create a course
# POST /api/courses/
@app.route('/api/courses/', methods=['POST'])
def create_course():
    post_body = json.loads(request.data)
    code = post_body.get('code', '')
    name = post_body.get('name', '')
    course = Course(code=code, name=name)
    db.session.add(course)
    db.session.commit()
    return json.dumps({'success': True, 'data': course.serialize()}), 201

# Get a specific course
# GET /api/course/{id}/
@app.route('/api/course/<int:course_id>/')
def get_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return json.dumps({'success': False, 'error': 'Course not found.'}), 404
    return json.dumps({'success': True, 'data': course.serialize()}), 200

# Create a user
# POST /api/users/
@app.route('/api/users/', methods=['POST'])
def create_user():
    post_body = json.loads(request.data)
    user = User(
        name=post_body.get('name', ''),
        netid=post_body.get('netid', '')
    )
    db.session.add(user)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 201

# Get a specific user
# GET /api/user/{id}/
@app.route('/api/user/<int:user_id>/')
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return json.dumps({'success': False, 'error': 'User not found.'}), 404
    return json.dumps({'success': True, 'data': user.serialize()}), 200

# Add a user to a specific course
# POST /api/course/{course_id}/add/
@app.route('/api/course/<int:course_id>/add/', methods=['POST'])
def add_user_to_course(course_id):
    post_body = json.loads(request.data)
    user_id = post_body.get('user_id', '')
    t = post_body.get('type', '')
    user = User.query.filter_by(id=user_id).first()
    course = Course.query.filter_by(id=course_id).first()
    if not course or not user:
        return json.dumps({'success': False, 'error': 'Course or User not found.'}), 404
    if t != 'student' and t != 'instructor':
        return json.dumps({'success': False, 'error': 'Type should be \'instructor\' or \'student\'.'}), 404
    if t == 'student':
        course.students.append(user)
    elif t == 'instructor':
        course.instructors.append(user)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 200

# Create an assignment for a course
# POST /api/course/{course_id}/assignment/
@app.route('/api/course/<int:course_id>/assignment/', methods=['POST'])
def create_assignment(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return json.dumps({'success': False, 'error': 'Course not found.'}), 404
    post_body = json.loads(request.data)
    due_date = datetime.strptime(post_body.get(
        'due_date', ''), '%m/%d/%Y').timestamp()
    assignment = Assignment(
        title=post_body.get('title', ''),
        due_date=due_date,
        course=course_id
    )
    course.assignments.append(assignment)
    db.session.add(assignment)
    db.session.commit()
    a = assignment.serialize()
    a['course'] = course.simplified()
    return json.dumps({'success': True, 'data': a}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
