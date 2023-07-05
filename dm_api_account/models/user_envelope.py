from enum import Enum
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool, StrictInt


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: StrictBool
    quality: StrictInt
    quantity: StrictInt


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl")
    status: Optional[StrictStr]
    rating: Rating
    online: Optional[datetime]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[datetime]


class UserEnvelope:
    resource: User
    metadata: Optional[StrictStr]
