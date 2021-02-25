import fastapi
import uvicorn

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
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

uvicorn.run(app=app_api)