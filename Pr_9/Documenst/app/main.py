from fastapi import FastAPI, HTTPException
import sys

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

sys.path.append('app')
from Documents import Document

documents: list[Document] = [
    Document(id=0, title='Document 1', content="Document 1 description"),
    Document(id=1, title='Document 2', content="Document 2 description"),
]

app = FastAPI()

app.mount("/app/pages", StaticFiles(directory="app/pages"), name="pages")


@app.get("/")
async def hello_creen():
    return FileResponse('app/pages/index.html')


@app.get("/v1/documents")
async def get_docs():
    return documents


@app.get("/v1/documents/{id}")
async def get_docs_by_id(id: int):
    result = [doc for doc in documents if doc.id == id]
    return result[0] if len(result) > 0 else HTTPException(status_code=404, detail=f"Document {id} not found")
