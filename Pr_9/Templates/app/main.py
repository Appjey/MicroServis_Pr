from fastapi import FastAPI, HTTPException
import sys

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

sys.path.append('app')
from Templates import Template

template: list[Template] = [
    Template(id=666, title='Template 1', content="Template 1 description"),
    Template(id=777, title='Template 2', content="Template 2 description"),
]

app = FastAPI()

app.mount("/app/pages", StaticFiles(directory="app/pages"), name="pages")


@app.get("/")
async def hello_creen():
    return FileResponse('app/pages/index.html')


@app.get("/v2/templates")
async def get_docs():
    return template


@app.get("/v2/templates/{id}")
async def get_docs_by_id(id: int):
    result = [templ for templ in template if templ.id == id]
    return result[0] if len(result) > 0 else HTTPException(status_code=404, detail=f"Template {id} not found")
