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

@app.post("/deliverActCode")
async def deliverActCode():
    return {"responseInfo": {
   "responseUID": "user0016-lgkj-7777-7777-123456789aze",
   "resultID": "ProceedWithSuccess",
   "errorCode": "00000",
   "errorDescription": "ProceedWithSuccess"
},
    "stepUpMethodExpirationTime": "2010-02-08T11:04:50.001Z",
    "activationCodeLength": "10"
}

@app.post("/verifyActivationCode")
async def deliverActCode():
    return {"responseInfo": {
   "responseUID": "user0016-lgkj-7777-7777-123456789aze",
   "resultID": "ProceedWithSuccess",
   "errorCode": "00000",
   "errorDescription": "ProceedWithSuccess"
},
  "verificationResult": "1"
}
