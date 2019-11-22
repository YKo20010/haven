from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

save_association = db.Table(
    'save_association',
    db.Model.metadata,
    db.Column('listing_id', db.Integer, db.ForeignKey('listing.id')),
    db.Column('collection_id', db.Integer, db.ForeignKey('collection.id'))
)


class Listing(db.Model):
    __tablename__ = 'listing'
    id = db.Column(db.Integer, primary_key=True)
    # TODO: update user_id to be relationship with user.id
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    is_draft = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String, nullable=True)
    rent = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String, nullable=False)
    collections = db.relationship(
        'Collection', secondary=save_association, back_populates='listings')

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', -1)
        self.title = kwargs.get('title', '')
        self.is_draft = kwargs.get('is_draft', True)
        self.description = kwargs.get('description', None)
        self.rent = kwargs.get('rent', None)
        self.address = kwargs.get('address', '')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'is_draft': self.is_draft,
            'description': self.description,
            'rent': self.rent,
            'address': self.address
        }


class Collection(db.Model):
    __tablename__ = 'collection'
    id = db.Column(db.Integer, primary_key=True)
    # TODO: update user_id to be relationship with user.id
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    listings = db.relationship(
        'Listing', secondary=save_association, back_populates='collections')

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', -1)
        self.title = kwargs.get('title', '')
        self.is_draft = kwargs.get('is_draft', True)
        self.description = kwargs.get('description', '')
        self.rent = kwargs.get('rent', -1)
        self.address = kwargs.get('address', '')
        self.listings = kwargs.get('listings', [])

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'is_draft': self.is_draft,
            'description': self.description,
            'rent': self.rent,
            'address': self.address
        }

# class Course(db.Model):
#     __tablename__ = 'course'
#     id = db.Column(db.Integer, primary_key=True)
#     code = db.Column(db.String, nullable=False)
#     name = db.Column(db.String, nullable=False)
#     assignments = db.relationship('Assignment', cascade='delete')
#     instructors = db.relationship(
#         'User', secondary=instructor_association, back_populates='teaching')
#     students = db.relationship(
#         'User', secondary=student_association, back_populates='taking')

#     def __init__(self, **kwargs):
#         self.code = kwargs.get('code', '')
#         self.name = kwargs.get('name', '')
#         self.assignments = kwargs.get('assignments', [])

#     def simplified(self):
#         return {
#             'id': self.id,
#             'code': self.code,
#             'name': self.name
#         }

#     def serialize(self):
#         return {
#             'id': self.id,
#             'code': self.code,
#             'name': self.name,
#             'assignments': [a.serialize() for a in self.assignments],
#             'instructors': [i.simplified() for i in self.instructors],
#             'students': [s.simplified() for s in self.students]
#         }


# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     netid = db.Column(db.String, nullable=False)
#     teaching = db.relationship(
#         'Course', secondary=instructor_association, back_populates='instructors')
#     taking = db.relationship(
#         'Course', secondary=student_association, back_populates='students')

#     def __init__(self, **kwargs):
#         self.name = kwargs.get('name', '')
#         self.netid = kwargs.get('netid', '')

#     def simplified(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'netid': self.netid
#         }

#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'netid': self.netid,
#             'courses': [c.simplified() for c in self.teaching].__add__([c.simplified() for c in self.taking])
#         }


# # One to many: course to assignments.
# class Assignment(db.Model):
#     __tablename__ = 'assignment'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     # Change to unix time.
#     due_date = db.Column(db.Integer, nullable=False)
#     # course_id
#     course = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

#     def __init__(self, **kwargs):
#         self.title = kwargs.get('title', '')
#         # Change to unix time.
#         self.due_date = kwargs.get('due_date', '')

#     def serialize(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'due_date': self.due_date,
#             'course': self.course
#         }
