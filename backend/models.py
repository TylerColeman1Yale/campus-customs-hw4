from pydantic import BaseModel, Field
from typing import Optional

class UserOut(BaseModel):
    id: int; first_name: str; last_name: str; email: str

class AuthRequest(BaseModel):
    email: str; password: str

class RegisterRequest(BaseModel):
    first_name: str; last_name: str; email: str; password: str

class Product(BaseModel):
    product_id: str; name: str; garment_type: str; description: str
    colors: str; image_file_path: str; price: float
    inventory: dict[str, int] = Field(default_factory=dict)

class ChatRequest(BaseModel):
    message: str; user_id: Optional[int] = None; product_id: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str; products: list[Product] = Field(default_factory=list)

class ChatContext(BaseModel):
    user: Optional[UserOut] = None; product: Optional[Product] = None
