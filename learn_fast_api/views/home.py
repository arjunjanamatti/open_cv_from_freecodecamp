import fastapi
import uvicorn
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates('templates')

router = fastapi.APIRouter()

@router.get(path='/')
def index(request: Request):
    return templates.TemplateResponse(name='index.html',context={'request': request})
    # return {
    #     'message': 'Testing with Fast API',
    #     'status': 'OK'
    # }
