from typing import Optional
from pydantic import BaseModel

class  User(BaseModel):
    id: int
    name: Optional[str]
    area: Optional[str]
    job_description: Optional[str]
    role: Optional[int] 
    salary: Optional[float]
    is_active: Optional[bool]
    last_evaluation: Optional[str]