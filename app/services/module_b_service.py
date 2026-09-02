from app.ml.module_b.engine import ModuleBEngine
from app.ml.module_b.mock_engine import MockModuleBEngine
from app.schemas.module_b import (
    ModuleBRequest,
    ModuleBResponse
)


class ModuleBService:

    def __init__(self, engine: ModuleBEngine | None = None):

        self.engine = (
            engine
            if engine is not None
            else MockModuleBEngine()
        )

    def predict(
        self,
        data: ModuleBRequest
    ) -> ModuleBResponse:

        return self.engine.predict(data)