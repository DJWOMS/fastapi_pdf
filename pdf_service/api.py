from fastapi import APIRouter
from starlette.responses import FileResponse

from . import schemas, services


pdf = APIRouter()


@pdf.post('/', response_model=schemas.DocOut)
async def doc_create(doc: schemas.Doc):
    return await services.create_doc(doc)


@pdf.get('/{pk}')
async def create_pdf(pk: int):
    return FileResponse(await services.create_pdf(pk))






