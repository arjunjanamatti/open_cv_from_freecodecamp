import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get(path='/items/{item_id}')
def read_item(item_id):
    return {
        'item_id':item_id
    }

uvicorn.run(app=api)