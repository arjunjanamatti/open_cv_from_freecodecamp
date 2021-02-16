import fastapi
import uvicorn
import views.home


api = fastapi.FastAPI()

def configure():
    api.include_router()

uvicorn.run(app=api)