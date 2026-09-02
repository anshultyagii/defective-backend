from pathlib import Path

from app.ml.module_a.engine import ModuleAEngine
from app.schemas.module_a import ModuleAResponse


class ProductionModuleAEngine(ModuleAEngine):

    def __init__(self, model_dir: Path):

        self.model_dir = model_dir

        # ==========================================
        # PLACEHOLDER
        # ==========================================
        #
        # We will load the actual Module A artifacts
        # here after the model is finalized.
        #
        # Example future artifacts:
        #
        # self.expected_value_model
        # self.scaler
        # self.isolation_forest
        # self.autoencoder
        # self.threshold
        #
        # ==========================================

    def predict(self, data) -> ModuleAResponse:

        raise NotImplementedError(
            "Final Module A model is not connected yet."
        )