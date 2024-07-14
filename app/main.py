from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from env import MONGODB_URl

client = MongoClient(MONGODB_URl)
db = client['para_user']

app = FastAPI()


@app.get("/") #기본 url
def home():
    return FileResponse("./Front/index.html")

@app.get("/login")
def 로그인():
    return FileResponse("./Front/signup.html")

@app.post("/signup_submit")
async def 회원가입(id:str = Header(None),pw:str=Header(None)):
    
    
    # MongoDB에 문서 추가
    result = client['para_user'].insert_one({"id": id, "password": pw})
    
    # # 삽입된 문서의 ID 반환
    inserted_id = str(result.inserted_id)
    
    return {"message": "회원가입이 완료되었습니다.", "inserted_id": inserted_id}


    #return user_document