from pydantic import BaseModel, StrictStr


class ChangeEmail(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr
