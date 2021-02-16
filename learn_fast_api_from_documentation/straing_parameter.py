import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get(path='/items/{item_id}')
def read_item(item_id):
    return {
        'item_id':item_id
    }
@api.get(path='/square/{item_id}')
def read_int_item(item_id:int):
    return {
        'square of number':item_id**2
    }

uvicorn.run(app=api)