from pathlib import Path

from app.ml.module_b.engine import ModuleBEngine
from app.schemas.module_b import ModuleBResponse


class ProductionModuleBEngine(ModuleBEngine):
    """
    Production adapter for the finalized Module B model.

    The actual model-loading and inference logic will be added
    once Module B has been finalized.
    """

    def __init__(self, model_dir: Path):

        self.model_dir = model_dir

        # ==========================================
        # PLACEHOLDER
        # ==========================================
        #
        # Future artifacts may include:
        #
        # self.predictor
        # self.scaler
        # self.safety_slope
        # self.feature_config
        # self.metadata
        #
        # These will be determined from the final
        # Module B training pipeline.
        #
        # ==========================================

    def predict(self, data) -> ModuleBResponse:

        raise NotImplementedError(
            "Final Module B model is not connected yet."
        )