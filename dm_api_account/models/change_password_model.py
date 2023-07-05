from pydantic import BaseModel, StrictStr


class ChangePassword(BaseModel):
    login: StrictStr
    token: StrictStr
    oldPassword: StrictStr
    newPassword: StrictStr
