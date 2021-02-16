import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get(path='/')
def index():
    return {
        'message': 'Testing with Fast API',
        'status': 'OK'
    }
    pass


uvicorn.run(app=api, host='localhost',port=8000)