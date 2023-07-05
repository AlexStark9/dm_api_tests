from enum import Enum
from pydantic import BaseModel, StrictStr, Field, StrictInt, StrictBool
from datetime import datetime
from typing import List, Optional


class PagingSettings(BaseModel):
    posts_per_page: StrictInt = Field(alias='postsPerPage')
    comments_per_page: StrictInt = Field(alias='commentsPerPage')
    topics_per_page: StrictInt = Field(alias='topicsPerPage')
    messages_per_page: StrictInt = Field(alias='messagesPerPage')
    entities_per_page: StrictInt = Field(alias='entitiesPerPage')


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class UserSettings(BaseModel):
    color_schema: ColorSchema = Field(alias='colorSchema')
    nanny_greetings_message: StrictStr = Field(alias='nannyGreetingsMessage')
    paging: PagingSettings


class InfoBbText(BaseModel):
    value: StrictStr
    parse_mode: StrictStr = 'Common'  # StrictStr=','


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


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl')
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl')
    status: Optional[StrictStr]
    rating: Rating
    online: Optional[datetime]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[datetime]
    icq: Optional[StrictStr]
    skype: Optional[StrictStr]
    original_picture_url: Optional[StrictStr] = Field(alias='originalPictureUrl')
    info: InfoBbText
    settings: UserSettings


class UserDetailsEnvelope(BaseModel):
    resource: UserDetails
    metadata: Optional[StrictStr]
