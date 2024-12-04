from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import HTTPException,APIRouter, Request, Response, Form, Cookie, Depends, status

from user_db import register_user, authenticate_user, log_activity


load_dotenv()
sessions = {}
templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def register_user_form(username: str = Form(...), password: str = Form(...)):
    if not register_user(username, password):
        raise HTTPException(status_code=400, detail="Username already exists")
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

@router.post("/login")
async def login_user(response: Response, username: str = Form(...), password: str = Form(...)):
    if not authenticate_user(username, password):
        return RedirectResponse(url="/login", status_code=status.HTTP_301_MOVED_PERMANENTLY)
    sessions[username] = True
    redirect_response = RedirectResponse(url="/secure", status_code=status.HTTP_303_SEE_OTHER)
    redirect_response.set_cookie(key="username", value=username)
    return redirect_response

def get_current_username(username: str = Cookie(None)):
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return username

@router.get("/secure")
async def secure_page(request: Request, username: str = Depends(get_current_username)):
    if username not in sessions:
        return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)

    log_activity("secure_page_access", username)
    return templates.TemplateResponse("secure.html", {"request": request, "username": username})

@router.get("/logout", response_class=RedirectResponse)
async def logout_user(response: Response):
    response.delete_cookie("username")
    return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
