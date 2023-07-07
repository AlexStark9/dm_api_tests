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
    enabled: Optional[StrictBool]
    quality: Optional[StrictInt]
    quantity: Optional[StrictInt]


class User(BaseModel):
    login: Optional[StrictStr] = Field(None, description='Login')
    roles: Optional[List[Roles]] = Field(None, description='Roles')
    medium_picture_url: Optional[StrictStr] = Field(None, alias='mediumPictureUrl',
                                                    description='mediumPictureUrl')
    small_picture_url: Optional[StrictStr] = Field(None, alias='smallPictureUrl',
                                                   description='smallPictureUrl')
    status: Optional[StrictStr] = Field(None, description='status')
    rating: Optional[Rating] = None
    online: Optional[datetime] = Field(None, description='online')
    name: Optional[StrictStr] = Field(None, description='name')
    location: Optional[StrictStr] = Field(None, description='location')
    registration: Optional[datetime] = Field(None, description='registration')


class UserEnvelope(BaseModel):
    resource: Optional[User]
    metadata: Optional[StrictStr] = Field(None, description='metadata')
