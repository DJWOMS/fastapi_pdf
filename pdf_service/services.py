import ormar
from fastapi import HTTPException
from fpdf import FPDF
from . import schemas, models


class PDF(FPDF):
    def titles(self, title):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt=title, border=0)

    def texts(self, text):
        self.set_xy(10.0, 40.0)
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)


async def create_doc(doc: schemas.Doc) -> models.Doc:
    return await models.Doc.objects.create(**doc.dict())


async def create_pdf(pk: int) -> str:
    try:
        _doc = await models.Doc.objects.get(id=pk)
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail="Not found")

    path = f'static/{_doc.title}.pdf'
    _pdf = PDF()
    _pdf.add_page()
    _pdf.titles(_doc.title)
    _pdf.texts(_doc.text)
    _pdf.set_author(_doc.author)
    _pdf.output(path, 'F')
    return path

