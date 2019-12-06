# Haven Backend API
Backend for posting/deleting/editing listings.

#### Tools:
&#10141; [SQLAlchemy](https://www.sqlalchemy.org/) - The ORM used
&#10141; [Flask](http://flask.pocoo.org/) - Web framework
&#10141; [Docker](https://www.docker.com/) - Containerization
&#10141; [Google Cloud](https://cloud.google.com/) - Server hosting

#### Authors:
&#10141; [Yanlam Ko](https://github.com/YKo20010)
&#10141; [Jack Thompson](https://github.com/jackthmp)

### See spec with [Dropbox](https://paper.dropbox.com/doc/Haven-Backend-API-WIP--Ap~_M5FNn_hdIArbDOHjuTmJAQ-bpk7vUlUZVoWzgrtHKBlf)

## Users
- GET all users:  `/api/users/`
- GET user by user_id: `/api/user/<user_id>/`
- POST user: `/api/users/`
- DELETE user by user_id:  `/api/user/<user_id>/`

### Get all users
#### Request: `GET /api/users/`
#### Response:

    {
      "success": True,
      "data": [ <USERS> ]
    }
    
### Get a user by user_id
#### Request: `GET /api/user/<user_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "name": "Jack",
        "drafts": [ <DRAFTED LISTINGS> ],
        "listings": [ <LISTINGS> ],
        "collections": [ <COLLECTIONS> ]
      }
    }

### Add a user
#### Request: `POST /api/users/`
#### Body:

    {
      "name": "Jack"
    }

#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "name": "Jack",
        "drafts": [],
        "listings": [],
        "collections": []
      }
    }
    
### Delete a user by user_id

#### Request: `GET /api/user/<user_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "name": "Jack",
        "drafts": [ <DRAFTED LISTINGS> ],
        "listings": [ <LISTINGS> ],
        "collections": [ <COLLECTIONS> ]
      }
    }
    
## Listings
- GET all listings: `/api/listings/`
- GET all listings by user_id: `/api/user/<user_id>/listings/`
- GET listing by listing_id: `/api/listing/listing_id>/`
- POST listing by user_id: `/api/user/<user_id>/listings/`
- POST (edit) listing by listing_id: `/api/listing/<listing_id>/`
- DELETE listing by listing_id: `/api/listing/<listing_id>/`

### Get all listings
#### Request: `GET /api/listings/`
#### Response:

    {
      "success": True,
      "data": [ <LISTINGS> ]
    }
    
### Get listings by user_id
- includes both published and drafts
#### Request: `GET /api/user/<user_id>/listings/`
#### Response:

    {
      "success": True,
      "data": [ <LISTINGS> ]
    }
    
### Get a listing by listing_id
- includes both published and drafts
#### Request: `GET /api/listing/<listing_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spacious 2BR Apt. in the heart of Collegetown",
        "is_draft": false,
        "description": "All new, fully furnished apartment.\n 5 minutes from the engineering quad.",
        "rent": 1050,
        "address": "717 E. Buffalo Street",
        "images": [ <IMAGES> ],
        "collections": [ <COLLECTIONS> ]
      }
    }
    
### Delete a listing by listing_id
- includes both published and drafts
#### Request: `DELETE /api/listing/<listing_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spacious 2BR Apt. in the heart of Collegetown",
        "is_draft": false,
        "description": "All new, fully furnished apartment.\n 5 minutes from the engineering quad.",
        "rent": 1050,
        "address": "717 E. Buffalo Street",
        "images": [ <IMAGES> ],
        "collections": [ <COLLECTIONS> ]
      }
    }
    
### Add a listing by user_id
#### Request: `POST /api/user/<user_id>/listings/`
#### Body:

    {
      "title": "Spacious 2BR Apt. in the heart of Collegetown",
      "is_draft": false,
      "description": "All new, fully furnished apartment.\n 5 minutes from the engineering quad.",
      "rent": 1050,
      "address": "717 E. Buffalo Street"
    }

#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spacious 2BR Apt. in the heart of Collegetown",
        "is_draft": False
        "description": "All new, fully furnished apartment.\n 5 minutes from the engineering quad.",
        "rent": 1050,
        "address": "717 E. Buffalo Street",
        "images": [ <IMAGES> ],
        "collections": [ <COLLECTIONS> ]
      }
    }
    
### Save a draft by user_id
- (same as Add a listing, but fewer info needed)
#### Request: `POST /api/user/<user_id>/listings/`
#### Body:

    {
      "title": "Spacious 2BR Apt. in the heart of Collegetown",
      "address": "717 E. Buffalo Street",
      "is_draft": True
    }

#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spacious 2BR Apt. in the heart of Collegetown",
        "is_draft": True
        "description": "",
        "rent": -1,
        "address": "717 E. Buffalo Street",
        "images": [ <IMAGES> ],
        "collections": [ <COLLECTIONS> ]
      }
    }
    
### Edit a listing by listing_id
- (ie. allow to post listing from draft)
#### Request: `POST /api/listing/<listing_id>/`
#### Body:

    {
      "title": "New or Old title", #optional
      "address": "New or Old address", #optional
      "is_draft": False, #optional
      "description": "New or Old description", #optional
      "rent": 1050, #optional
    }

#### Response:

    {
      "success": True,
      "data": {
        "id": <listing_id>,
        "user_id": <user_id>,
        "title": "New or Old title",
        "is_draft": True
        "description": "New or Old description",
        "rent": 1050,
        "address": "New or Old address",
        "images": [ <IMAGES> ],
        "collections": [ <COLLECTIONS> ]
      }
    }


## Collections
- GET collections by user_id: `/api/user/<user_id>/collections/`
- GET collection by collection_id: `/api/collection/<collection_id>/`
- POST collection by user_id: `/api/user/<user_id>/collections/`
- DELETE collection by collection_id: `/api/collection/<collection_id>/`
- POST listing to collection by collection_id: `/api/collection/<collection_id>`

### Get collections by user_id
#### Request: `GET /api/user/<user_id>/collections/`
#### Response:

    {
      "success": True,
      "data": [ <COLLECTIONS> ]
    }
    
### Get a collection by collection_id
#### Request: `GET /api/collection/<collection_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user": 1,
        "title": "Spring 2020",
        "listings": [ <LISTINGS> ]
      }
    }

### Add a collection by user_id
#### Request: `POST /api/user/<user_id>/collections/`
#### Body:

    {
      "title": "Spring 2020"
    }

#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spring 2020",
        "listings": []
      }
    }
    
### Delete a collection by collection_id
#### Request: `DELETE /api/collection/<collection_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user": 1,
        "title": "Spring 2020",
        "listings": [ <LISTINGS> ]
      }
    }
    
### Save listing to collection by collection_id

#### Request: `POST /api/collection/<collection_id>`
#### Body:

    {
      "listing_id": 0
    }

#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spring 2020",
        "listings": [
          {
            "id": 0,
            "user_id": 1,
            "title": "Spacious 2BR Apt. in the heart of Collegetown"
          },
          ...
        ]
      }
    }


## Images
- GET images by listing_id: `/api/listing/<listing_id>/images/`
- GET image by image_id: `/api/image/<image_id>/`
- POST image by listing_id: `/api/listing/<listing_id>/images/`
- DELETE image by image_id: `/api/image/<image_id>/`

### Get images by listing_id
#### Request: `GET /api/listing/<listing_id>/images/`
#### Response:

    {
      "success": True, 
      "data": [
        {
          "id": 1, 
          "image": "456789086543456789fghjkkjhgfddfghjk", 
          "listing_id": 1
        }
      ]
    }
    
### Get a image by image_id

#### Request: `GET /api/image/<image_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "image": "AISHLKJNW8\][po3099ipoj33u9ISIDehjh189898 (image as a string)... ",
        "listing_id": 1
      }
    }
    
### Add image to listing by listing_id

#### Request: `POST /api/listing/<listing_id>/images/`
#### Body:

    {
        "image": "AISHLKJNW8\po3099ipoj33u9ISIDehjh189898 (image as a string)... "
    }

#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "image": "AISHLKJNW8\po3099ipoj33u9ISIDehjh189898 (image as a string)... ",
        "listing_id": 1
      }
    }
    
### Delete a image by image_id

#### Request: `DELETE /api/image/<image_id>/`
#### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "image": "AISHLKJNW8\po3099ipoj33u9ISIDehjh189898 (image as a string)... ",
        "listing_id": 1
      }
    }
