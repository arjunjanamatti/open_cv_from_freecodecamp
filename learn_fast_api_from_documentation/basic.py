from fastapi import FastAPI
import uvicorn

api = FastAPI()


@api.post(path='/')
def index():
    return {
        'message': 'Hello World',
        'status': 'OK'
    }

uvicorn.run(app=api)