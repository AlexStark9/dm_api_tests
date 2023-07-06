from pydantic import StrictStr, BaseModel, StrictBool


class LoginCredentials(BaseModel):
    login: StrictStr
    password: StrictStr
    rememberMe: StrictBool
