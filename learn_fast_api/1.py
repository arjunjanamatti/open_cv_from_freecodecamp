import fastapi
import uvicorn


api = fastapi.FastAPI()

@api.get(path='/api/calculate')
def calculate():
    return 5*5

uvicorn.run(app=api,host='127.0.0.1',port=8000)