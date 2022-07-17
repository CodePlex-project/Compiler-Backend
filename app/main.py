from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from compylex.compiler import Compile
import json


class Item(BaseModel):
    code: str
    lang: str
    input: str
    id: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/compile/")
async def create_item(item: Item):
    result = Compile(item.code, item.lang, item.input, item.id)
    output = result.get_output()
    status = result.get_status()
    data = {
        "output": output,
        "status": status,
    }
    data = json.dumps(data)
    return data
