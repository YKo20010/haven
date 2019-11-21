# haven
Haven backend.
Haven Backend API (WIP)

## Get all users

### Request: `GET /api/users/`
### Response:

    {
      "success": True,
      "data": [ <USERS> ]
    }
    
## Get a specific user

### Request: `GET /api/user/<``user_``id>/`
### Response:

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


## Get all listings

### Request: `GET /api/listings/`
### Response:

    {
      "success": True,
      "data": [ <LISTINGS> ]
    }
## Get all listings per user

 ### Request: `GET /api/``user/<user_id>/listings``/`
 ### Response:

    {
      "success": True,
      "data": [ <LISTINGS> ]
    }
    
## Get all drafts per user

### Request: `GET /api/``user/<user_id>/drafts``/`
### Response:

    {
      "success": True,
      "data": [ <LISTINGS> ]
    }

## Get a specific listing

### Request: `GET /api/listing/<``listing_``id>/`
### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spacious 2BR Apt. in the heart of Collegetown",
        "description": "All new, fully furnished apartment.\n 5 minutes from the engineering quad.",
        "rent": 1050,
        "address": "717 E. Buffalo Street",
        "latitude": 42.4414283, # optional?
        "longitude": -76.4876436, # optional?
      }
    }
    
## Post a listing

### Request: `POST /api/``user/<user_id>/``listings/`
### Body:

    {
      "user_id": 1,
      "title": "Spacious 2BR Apt. in the heart of Collegetown",
      "is_draft": False
      "description": "All new, fully furnished apartment.\n 5 minutes from the engineering quad.",
      "rent": 1050,
      "address": "717 E. Buffalo Street",
      "latitude": 42.4414283, # optional?
      "longitude": -76.4876436, # optional?
    }

### Response:

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
        "latitude": 42.4414283, # optional?
        "longitude": -76.4876436, # optional?
      }
    }
    
## Save a draft

### Request: `POST /api/``user/<user_id>/``listings/`
### Body:

    {
      "user_id": 1,
      "title": "Spacious 2BR Apt. in the heart of Collegetown",
      "address": "717 E. Buffalo Street",
      "is_draft": True
    }

### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spacious 2BR Apt. in the heart of Collegetown",
        "is_draft": True
        "description": "",
        "rent": -1,
        "address": "717 E. Buffalo Street"
      }
    }
    
## Search listings

### Request: `GET /api/listings/search?q=<query>`
### Body:

    {
      "max_price": 2000,
      "filter2": ...
    }

### Response:

    {
      "success": True,
      "data": {
        "listings": [ <LISTINGS> ]
        "query": "buffalo"
        "applied_filters": {
          "max_price": 2000,
          "filter2":
        }
      }
    }


## Get all collections per user

 ### Request: `GET /api/``user/<user_id>/collections``/`
 ### Response:

    {
      "success": True,
      "data": [ <COLLECTIONS> ]
    }
    
## Get a specific collection

### Request: `GET /api/``collections``/<``collection_id``>/`
### Response:

    {
      "success": True,
      "data": {
        "id": 0,
        "user_id": 1,
        "title": "Spring 2020",
        "listings": [ <LISTINGS> ]
      }
    }
