# Todo-app backend


APIS

    1. Listing todo rows.

    Method: GET
    Url: http://35.233.8.56/api/todo/?format=json
    Example Response (200):
    [
        {
        id: 1,
        is_active: true,
        created_at: "2021-05-05T00:56:20.723815Z",
        updated_at: "2021-05-05T00:56:20.723901Z",
        title: "buy some milk",
        is_completed: false
        }
    ]


    2. Create new todo
    Method: POST
    Url: http://35.233.8.56/api/todo/
    Example Response (201):
    {
        "id":1,
        "is_active":true,
        "created_at":"2021-05-05T00:56:20.723815Z",
        "updated_at":"2021-05-05T00:56:20.723901Z",
        "title":"buy some milk",
        "is_completed":false
    }


## Build and Start Backend Container
```
docker-compose up --build
```


## Testing
```
python manage.py test
```
