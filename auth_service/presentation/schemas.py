from pydantic import BaseModel, Field


class APIKeySchema(BaseModel):
    api_key: str = Field(
        max_length=256,
        min_length=256,
        description="Only 256 characters are allowed for the api key",
    )
