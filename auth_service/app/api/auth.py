from fastapi import FastAPI, APIRouter
from auth_service.app.api.models import UserSignUp, UserSignin

auth = FastAPI(title="Authentication Service", version="1.0.0", root_path="/api")

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register", tags=["Auth Service"])
def sign_up(payload: UserSignUp):
    """
    Create a new user in the database
    """
    # retrieve payload
    # check if user's email exist in the backend
    # hash password
    # save hashed password and email in backend
    # create token with jwt
    # return token in response
    pass


@auth_router.post("/login", tags=["Auth Service"])
async def sign_in(payload: UserSignin):
    # retrieve payload
    # verify email exists in database
    # use bcrypt to check password
    # create token with jwt
    # return token in response
    pass


@auth_router.post("/logout", tags=["Auth Service"])
async def sign_out():
    # deactivate jwt
    # return response
    pass


auth.include_router(auth_router)
