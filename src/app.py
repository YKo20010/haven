import json
from db import db, Listing, Collection, User
from flask import Flask, request

db_filename = "todo.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# Get all users
# GET /api/users/
@app.route('/')
@app.route('/api/users/')
def get_users():
    users = User.query.all()
    res = {'success': True, 'data': [u.serialize() for u in users]}
    return json.dumps(res), 200

# Get a specific user
# GET /api/user/{user_id}/
@app.route('/api/user/<int:user_id>/')
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return json.dumps({'success': False, 'error': 'User not found.'}), 404
    return json.dumps({'success': True, 'data': user.serialize()}), 200

# Add a user
# POST /api/users/
@app.route('/api/users/', methods=['POST'])
def add_user():
    # TODO: implement route
    post_body = json.loads(request.data)
    user = User(
        name=post_body.get('name', '')
    )
    db.session.add(user)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 201

# Get all listings
# GET /api/listings/
@app.route('/api/listings/')
def get_listings():
    listings = Listing.query.all()
    res = {'success': True, 'data': [l.serialize() for l in listings]}
    return json.dumps(res), 200

# Get all listings per user
# GET /api/user/<user_id>/listings/
@app.route('/api/user/<int:user_id>/listings/')
def get_listings_by_user(user_id):
    # TODO: implement route
    return

# Get all drafts per user
# GET /api/user/<user_id>/drafts/
@app.route('/api/user/<int:user_id>/drafts/')
def get_drafts_by_user(user_id):
    # TODO: implement route
    return

# Get a specific listing
# GET /api/listing/<listing_id>/
@app.route('/api/listing/<int:listing_id>/')
def get_listing(listing_id):
    # TODO: implement route
    return

# Post a listing or draft
# POST /api/user/<user_id>/listings/
@app.route('/api/user/<int:user_id>/listings/', methods=['POST'])
def add_listing(user_id):
    # user = User.query.filter_by(id=user_id).first()
    # if not user:
    #     return json.dumps({'success': False, 'error': 'User not found.'}), 404
    post_body = json.loads(request.data)

    title = post_body.get('title', '')
    is_draft = post_body.get('is_draft', True)
    description = post_body.get('description', '')
    rent = post_body.get('rent', -1)
    address = post_body.get('address', '')

    listing = Listing(
        user_id=user_id, title=title, is_draft=is_draft,
        description=description, rent=rent, address=address)

    db.session.add(listing)
    db.session.commit()

    return json.dumps({'success': True, 'data': listing.serialize()}), 201

# Get all collections per user
# GET /api/user/<user_id>/collections/
@app.route('/api/user/<int:user_id>/collections/')
def get_collections_by_user(user_id):
        # TODO: implement route
    return

# Get a specific collection
# GET /api/user/<user_id>/collection/<collection_id>/
@app.route('/api/user/<int:user_id>/collection/<int:collection_id>')
def get_collection_by_user(user_id, collection_id):
        # TODO: implement route
    return

# Post a new collection
# POST /api/user/<user_id>/collections/
@app.route('/api/user/<int:user_id>/collections/')
def add_collection(user_id):
        # TODO: implement route
    return

# Save a listing to a collection
# POST /api/user/<user_id>/collection/<collection_id>
@app.route('/api/user/<int:user_id>/collection/<int:collection_id>', methods=['POST'])
def add_listing_to_collection(user_id, collection_id):
        # TODO: implement route
    return
    # post_body = json.loads(request.data)
    # user_id = post_body.get('user_id', '')
    # t = post_body.get('type', '')
    # user = User.query.filter_by(id=user_id).first()
    # course = Course.query.filter_by(id=course_id).first()
    # if not course or not user:
    #     return json.dumps({'success': False, 'error': 'Course or User not found.'}), 404
    # if t != 'student' and t != 'instructor':
    #     return json.dumps({'success': False, 'error': 'Type should be \'instructor\' or \'student\'.'}), 404
    # if t == 'student':
    #     course.students.append(user)
    # elif t == 'instructor':
    #     course.instructors.append(user)
    # db.session.commit()
    # return json.dumps({'success': True, 'data': user.serialize()}), 200

# Create an assignment for a course
# POST /api/course/{course_id}/assignment/
# @app.route('/api/course/<int:course_id>/assignment/', methods=['POST'])
# def create_assignment(course_id):
#     course = Course.query.filter_by(id=course_id).first()
#     if not course:
#         return json.dumps({'success': False, 'error': 'Course not found.'}), 404
#     post_body = json.loads(request.data)
#     due_date = datetime.strptime(post_body.get(
#         'due_date', ''), '%m/%d/%Y').timestamp()
#     assignment = Assignment(
#         title=post_body.get('title', ''),
#         due_date=due_date,
#         course=course_id
#     )
#     course.assignments.append(assignment)
#     db.session.add(assignment)
#     db.session.commit()
#     a = assignment.serialize()
#     a['course'] = course.simplified()
#     return json.dumps({'success': True, 'data': a}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
