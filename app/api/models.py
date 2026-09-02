from fastapi import APIRouter

from app.core.model_manager import ModelManager
from app.schemas.model_status import ModelStatusResponse


router = APIRouter(
    prefix="/api/v1/models",
    tags=["Models"]
)

model_manager = ModelManager()


@router.get(
    "",
    response_model=ModelStatusResponse
)
def get_model_status():

    return model_manager.get_status()