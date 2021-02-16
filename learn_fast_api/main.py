import fastapi
import uvicorn
import views.home


api = fastapi.FastAPI()

def configure():
    api.include_router(views.home.router)

configure()
if __name__=='__main__':
    uvicorn.run(app=api)