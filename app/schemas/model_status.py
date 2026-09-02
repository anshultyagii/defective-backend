from pydantic import BaseModel


class ModelInfo(BaseModel):
    version: str
    path: str
    available: bool


class ModelStatusResponse(BaseModel):
    module_a: ModelInfo
    module_b: ModelInfo