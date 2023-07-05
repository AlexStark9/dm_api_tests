from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool, StrictInt


# {
#   "message": "string",
#   "invalidProperties": {
#     "additionalProp1": ["string"],
#     "additionalProp2": ["string"],
#     "additionalProp3": ["string"]
#   }
# }
# Не уверен, что правилльно тут описал

class invalidProperties(BaseModel):
    additional_prop_1: List[str]
    additional_prop_2: List[str]
    additional_prop_3: List[str]


class BadRequestError(BaseModel):
    message: StrictStr
    invalid_properties: invalidProperties
