import time
from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm

from src.core import crud, models, schemas, security
from src.core.config import settings
from src.core.db import engine
from src.core.deps import CurrentUser, SessionDep
from src.core.schemas import Token

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/login/access-token/")
async def login(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:

    user = crud.authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return Token(
        access_token=security.create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )


@app.post("/singup", response_model=schemas.User)
async def create_user(session: SessionDep, user: schemas.UserCreate):
    db_user = crud.get_user(session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(session, user)


@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: CurrentUser, session: SessionDep):
    db_user = crud.get_user(session, user_id=current_user.id)
    return db_user


@app.get("/users/me/items/", response_model=list[schemas.Item])
async def read_own_items(
    session: SessionDep,
    current_user: CurrentUser,
    skip: int = 0,
    limit: int = 100,
):
    db_items = crud.get_items(
        session, user_id=current_user.id, skip=skip, limit=limit
    )

    return db_items


@app.middleware("http")
async def add_process_time_header_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
