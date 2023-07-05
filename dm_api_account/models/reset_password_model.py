from pydantic import BaseModel, StrictStr


class ResetPassword(BaseModel):
    login: StrictStr
    email: StrictStr
