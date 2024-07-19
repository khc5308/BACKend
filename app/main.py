from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient
import os   
from env import MONGOKEY
from fastapi.middleware.cors import CORSMiddleware


client = AsyncIOMotorClient(MONGOKEY)
db = client['para6']

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

@app.get("/")  # 기본 url
def home():
    return FileResponse("./Front/index.html")
@app.get("/logind")
def signup():
    return FileResponse("./Front/login_index.html")
@app.get("/signup")
def signup():
    return FileResponse("./Front/signup.html")
@app.get("/login")
def signup():
    return FileResponse("./Front/login.html")
@app.get("/exit")
def signup():
    return FileResponse("./Front/exit.html")
@app.get("/menu")
def menu():
    return FileResponse("./Front/menu.html")


@app.post("/signup_submit")
async def signup_submit(id: str = Header(None), pw: str = Header(None)):
    if not await db['para_user'].find_one({"id": id}):
        await db['para_user'].insert_one({"id": id, "password": pw})
        return RedirectResponse(url="/logind")

    else:
        return {"status": "failure", "message": "User already exists"}
    
@app.post("/login_submit")
async def login_submit(id: str = Header(None), pw: str = Header(None)):
    if await db['para_user'].find_one({"id": id, "password": pw}):
        return {"로그인 완료"}
    else:
      return {"error": "회원정보를 찾을 수 없음"}
    
@app.post("/exit_submit")
async def login_submit(id: str = Header(None), pw: str = Header(None)):
    if db['para_user'].find_one({"id": id, "password": pw}):
        db['para_user'].delete_one({"id": id, "password": pw})
    else:
        return {"비밀번호 혹은 id를 찾을 수 없습니다"}

@app.get("https://npi.ny64.kr/snt_lunch")
async def get_lunch(month: int, day: int):
    # 여기에 급식 데이터를 처리하는 로직을 추가합니다.
    return {"month": month, "day": day, "menu": "Sample Menu"}