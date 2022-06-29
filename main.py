from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import json
import os
app = FastAPI()

@app.get("/")
async def Home():
    return RedirectResponse("/docs")

@app.post("/test")
async def test(request:Request):
   item = await request.json()
   data1 = json.dumps(item["data"])
   data2 = json.loads(data1)
   f = open("main.py", "a")
   #f.write("from fastapi import FastAPI\napp = FastAPI()\n")
   f.write("\n@app."+item["verb"]+'("/'+item["url"]+'")\n')
   f.write("\nasync def "+ item["function"]+"():\n")
   f.write("\treturn " + data1+"\n\n")
   f.close()
   return data2

@app.post("/testurl")

async def test():
	return {"data": "7888"}

