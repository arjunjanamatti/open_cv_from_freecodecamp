import fastapi
import uvicorn
from typing import Optional

app_api = fastapi.FastAPI()

@app_api.get('/square_result/{item_id}')
def square_number(item_id: int):
    return {
        f'Square result of {item_id} is': item_id**2
    }

@app_api.get('/area_of_rectangle/{item_id_1}/{item_id_2}')
def RectangleArea(item_id_1: int, item_id_2: int):
    return {
        f'Area of rectangle with sides {item_id_1} and {item_id_2} is': item_id_1 * item_id_2
    }


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app_api.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app_api.get("/optional_items/")
async def optional_read_item(item_id: str = 'Arjun', optional_item: Optional[str]=None):
    if optional_item:
        return {
            'item_id': item_id,
            'optional_item': optional_item
        }
    return {
        'item_id': item_id
    }

# http://127.0.0.1:8000/optional_items/?item_id=fine&optional_item=arjun

# multiple parameters
@app_api.get('/multiple_users/{user_id}/multiple_items/{item_id}')
def multiple_items(user_id: str, item_id: str):
    return {
        'user_id': user_id,
        'item_id': item_id
    }

uvicorn.run(app=app_api)