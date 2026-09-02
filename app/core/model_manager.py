import logging
from pathlib import Path

from app.core.config import (
    MODELS_DIR,
    MODULE_A_VERSION,
    MODULE_B_VERSION,
)


logger = logging.getLogger(__name__)


class ModelManager:
    """
    Central manager for ML model versions.

    For now, this class only manages model paths and availability.
    Actual model loading will be added after Module A and Module B
    are finalized.
    """

    def __init__(self):

        self.module_a_model = None
        self.module_b_model = None

    # ==========================================
    # MODULE A PATH
    # ==========================================

    def get_module_a_path(self) -> Path:

        return (
            MODELS_DIR
            / "module_a"
            / MODULE_A_VERSION
        )

    # ==========================================
    # MODULE B PATH
    # ==========================================

    def get_module_b_path(self) -> Path:

        return (
            MODELS_DIR
            / "module_b"
            / MODULE_B_VERSION
        )

    # ==========================================
    # CHECK MODEL DIRECTORIES
    # ==========================================

    def load_models(self):

        module_a_path = self.get_module_a_path()
        module_b_path = self.get_module_b_path()

        logger.info(
            "Module A model path: %s",
            module_a_path
        )

        logger.info(
            "Module B model path: %s",
            module_b_path
        )

        # We are intentionally NOT loading the actual ML models yet.
        # Module A and Module B are still being fine-tuned.

        if module_a_path.exists():
            logger.info(
                "Module A version %s is available.",
                MODULE_A_VERSION
            )
        else:
            logger.warning(
                "Module A version %s is not available yet.",
                MODULE_A_VERSION
            )

        if module_b_path.exists():
            logger.info(
                "Module B version %s is available.",
                MODULE_B_VERSION
            )
        else:
            logger.warning(
                "Module B version %s is not available yet.",
                MODULE_B_VERSION
            )

    # ==========================================
    # MODEL STATUS
    # ==========================================

    def get_status(self):

        module_a_path = self.get_module_a_path()
        module_b_path = self.get_module_b_path()

        return {
            "module_a": {
                "version": MODULE_A_VERSION,
                "path": str(module_a_path),
                "available": module_a_path.exists(),
            },

            "module_b": {
                "version": MODULE_B_VERSION,
                "path": str(module_b_path),
                "available": module_b_path.exists(),
            },
        }