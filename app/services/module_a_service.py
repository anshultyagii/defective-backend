from app.ml.module_a.engine import ModuleAEngine
from app.ml.module_a.mock_engine import MockModuleAEngine
from app.schemas.module_a import (
    ModuleARequest,
    ModuleAResponse
)


class ModuleAService:

    def __init__(
        self,
        engine: ModuleAEngine | None = None
    ):

        self.engine = (
            engine
            if engine is not None
            else MockModuleAEngine()
        )

    def predict(
        self,
        data: ModuleARequest
    ) -> ModuleAResponse:

        return self.engine.predict(data)