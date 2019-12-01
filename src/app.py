import json
from db import db, Listing, Collection, User, Image
from flask import Flask, request

db_filename = "haven.db"
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
    post_body = json.loads(request.data)
    user = User(
        name=post_body.get('name', '')
    )
    db.session.add(user)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 201

# Delete a user
# DELETE /api/user/{user_id}/
@app.route('/api/user/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return json.dumps({'success': False, 'error': 'User not found.'}), 404
    db.session.delete(user)
    db.session.commit()
    return json.dumps({'success': True, 'data': user.serialize()}), 200

# Get all listings
# GET /api/listings/
@app.route('/api/listings/')
def get_listings():
    listings = Listing.query.all()
    res = {'success': True, 'data': [l.serialize() for l in listings]}
    return json.dumps(res), 200

# Get all listings and drafts per user
# GET /api/user/<user_id>/listings/
@app.route('/api/user/<int:user_id>/listings/')
def get_listings_by_user(user_id):
    listings = Listing.query.filter_by(
        user_id=user_id)
    res = {'success': True, 'data': [l.serialize() for l in listings]}
    return json.dumps(res), 200

# Get a specific listing
# GET /api/listing/<listing_id>/
@app.route('/api/listing/<int:listing_id>/')
def get_listing(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    if not listing:
        return json.dumps({'success': False, 'error': 'Listing not found.'}), 404
    return json.dumps({'success': True, 'data': listing.serialize()}), 200

# Post a listing or draft
# POST /api/user/<user_id>/listings/
@app.route('/api/user/<int:user_id>/listings/', methods=['POST'])
def add_listing(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return json.dumps({'success': False, 'error': 'User not found.'}), 404
    post_body = json.loads(request.data)

    title = post_body.get('title', '')
    is_draft = post_body.get('is_draft', True)
    description = post_body.get('description', '')
    rent = post_body.get('rent', -1)
    address = post_body.get('address', '')

    listing = Listing(
        user_id=user_id, title=title, is_draft=is_draft,
        description=description, rent=rent, address=address)

    user.listings.append(listing)
    db.session.add(listing)
    db.session.commit()

    return json.dumps({'success': True, 'data': listing.serialize()}), 201

# Edit a listing
# POST /api/listing/<listing_id>/
@app.route('/api/listing/<int:listing_id>/', methods=['POST'])
def edit_listing(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    if not listing:
        return json.dumps({'success': False, 'error': 'Listing not found.'}), 404
    post_body = json.loads(request.data)

    listing.title = post_body.get('title', listing.title)
    listing.is_draft = post_body.get('is_draft', listing.is_draft)
    listing.description = post_body.get('description', listing.description)
    listing.rent = post_body.get('rent', listing.rent)
    listing.address = post_body.get('address', listing.address)
    db.session.commit()
    return json.dumps({'success': True, 'data': listing.serialize()}), 201

# Delete a listing
# DELETE /api/listing/<listing_id>/
@app.route('/api/listing/<int:listing_id>/', methods=['DELETE'])
def delete_listing(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    if not listing:
        return json.dumps({'success': False, 'error': 'Listing not found.'}), 404
    db.session.delete(listing)
    db.session.commit()
    return json.dumps({'success': True, 'data': listing.serialize()}), 200

# Get all collections per user
# GET /api/user/<user_id>/collections/
@app.route('/api/user/<int:user_id>/collections/')
def get_collections_by_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return json.dumps({'success': False, 'error': 'User not found.'}), 404
    collections = Collection.query.filter_by(user_id=user_id)
    return json.dumps({'success': True, 'data': [c.serialize() for c in collections]}), 200

# Get a specific collection
# GET /api/collection/<collection_id>/
@app.route('/api/collection/<int:collection_id>/')
def get_collection(collection_id):
    collection = Collection.query.filter_by(id=collection_id).first()
    if not collection:
        return json.dumps({'success': False, 'error': 'Collection not found.'}), 404
    return json.dumps({'success': True, 'data': collection.serialize()}), 200

# Post a new collection
# POST /api/user/<user_id>/collections/
@app.route('/api/user/<int:user_id>/collections/', methods=['POST'])
def add_collection(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return json.dumps({'success': False, 'error': 'User not found.'}), 404
    post_body = json.loads(request.data)
    title = post_body.get('title', '')
    collection = Collection(user_id=user_id, title=title)
    user.collections.append(collection)
    db.session.add(collection)
    db.session.commit()
    return json.dumps({'success': True, 'data': collection.serialize()}), 201

# Save a listing to a collection
# POST /api/collection/<collection_id>
@app.route('/api/collection/<int:collection_id>/', methods=['POST'])
def add_listing_to_collection(collection_id):
    collection = Collection.query.filter_by(id=collection_id).first()
    if not collection:
        return json.dumps({'success': False, 'error': 'Collection not found.'}), 404
    post_body = json.loads(request.data)
    listing_id = post_body.get('listing_id', '')
    listing = Listing.query.filter_by(id=listing_id).first()
    if not listing:
        return json.dumps({'success': False, 'error': 'Listing not found.'}), 404
    collection.listings.append(listing)
    db.session.commit()
    return json.dumps({'success': True, 'data': collection.serialize()}), 200

# Delete a collection
# DELETE /api/collection/<collection_id>/
@app.route('/api/collection/<int:collection_id>/', methods=['DELETE'])
def delete_collection(collection_id):
    collection = Collection.query.filter_by(id=collection_id).first()
    if not collection:
        return json.dumps({'success': False, 'error': 'Collection not found.'}), 404
    db.session.delete(collection)
    db.session.commit()
    return json.dumps({'success': True, 'data': collection.serialize()}), 200

# Create an image for a listing
# POST /api/listing/<listing_id>/images/
@app.route('/api/listing/<int:listing_id>/images/', methods=['POST'])
def add_image(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    if not listing:
        return json.dumps({'success': False, 'error': 'Listing not found.'}), 404
    post_body = json.loads(request.data)
    image = Image(
        image=post_body.get('image', ''),
        listing_id=listing_id
    )
    listing.images.append(image)
    db.session.add(image)
    db.session.commit()
    return json.dumps({'success': True, 'data': image.serialize()}), 201

# Get all images per listing
# GET /api/listing/<listing_id>/images/
@app.route('/api/listing/<int:listing_id>/images/')
def get_images(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    if not listing:
        return json.dumps({'success': False, 'error': 'Listing not found.'}), 404
    images = listing.images
    return json.dumps({'success': True, 'data': [i.serialize() for i in images]}), 200

# Get a specific image
# GET /api/image/<image_id>/
@app.route('/api/image/<int:image_id>/')
def get_image(image_id):
    image = Image.query.filter_by(id=image_id).first()
    if not image:
        return json.dumps({'success': False, 'error': 'Image not found.'}), 404
    return json.dumps({'success': True, 'data': image.serialize()}), 200

# Delete a image
# DELETE /api/image/<image_id>/
@app.route('/api/image/<int:image_id>/', methods=['DELETE'])
def delete_image(image_id):
    image = Image.query.filter_by(id=image_id).first()
    if not image:
        return json.dumps({'success': False, 'error': 'Image not found.'}), 404
    db.session.delete(image)
    db.session.commit()
    return json.dumps({'success': True, 'data': image.serialize()}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
