from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import HTTPException,APIRouter, Request, Response, Depends, status

from model import User
from jwt_auth import create_jwt_token, verify_jwt_token
from user_db import register_user, authenticate_user, log_activity


router = APIRouter()
templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def register_user_form(user: User):
    if not register_user(user):
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"message": "Registered successfully", "path": "/login"}

@router.post("/login")
async def login_user(user: User):
    if not authenticate_user(user):
        return RedirectResponse(url="/login", status_code=status.HTTP_301_MOVED_PERMANENTLY)

    response = RedirectResponse(url="/secure", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="username", value=user.username)

    auth_token = create_jwt_token({"sub": user.username})
    auth_response = {"auth_token": auth_token, "type": "bearer"}
    return auth_response

@router.get("/secure")
async def secure_page(request: Request, token: str = Depends(oauth2_scheme)):
    username = verify_jwt_token(token)
    log_activity("secure_page_access", username)
    return templates.TemplateResponse("secure.html", {"request": request, "username": username})

@router.get("/logout", response_class=RedirectResponse)
async def logout_user(response: Response):
    redirect_response = RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
    redirect_response.delete_cookie("username")
    return redirect_response
