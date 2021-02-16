import fastapi
import uvicorn
import enum

class ModelName(str,enum.Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

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

@api.get('/models/{model_name}')
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {
            'model_name': model_name,
            'message': 'Alex Net model name is selected'
        }
    elif model_name == ModelName.resnet:
        return {
            'model_name': model_name,
            'message': 'resnet model name is selected'
        }

uvicorn.run(app=api)