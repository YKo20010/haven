from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# student_association = db.Table(
#     'student_association',
#     db.Model.metadata,
#     db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
# )
# instructor_association = db.Table(
#     'instructor_association',
#     db.Model.metadata,
#     db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
# )


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
