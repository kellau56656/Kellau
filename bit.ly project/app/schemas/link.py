from pydantic import BaseModel

class LinkCreate(BaseModel):
    original_url: str