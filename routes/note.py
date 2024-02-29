from typing import Union
from fastapi import APIRouter,Request, FastAPI
from config.db import conn
from model.note import Note
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

note=APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    new_docs = []
    for doc in docs:
        title = doc.get("title", "Title Not Found")
        desc = doc.get("desc", "Description Not Found")
        important = doc.get("important", False)
        new_docs.append({
            "id": doc["_id"],
            "title": title,
            "desc": desc,
            "important": important
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": new_docs})




@note.post("/")
async def create_item(request:Request):
    form=await request.form()
    formDict=dict(form)
    formDict["important"]=False if formDict["important"]=="on" else False
    note=conn.notes.notes.insert_one(formDict)
    return {"success":True}
                                            