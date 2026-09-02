from pathlib import Path


# ==========================================
# PROJECT ROOT
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[2]


# ==========================================
# MODEL DIRECTORY
# ==========================================

MODELS_DIR = BASE_DIR / "models"


# ==========================================
# ACTIVE MODEL VERSIONS
# ==========================================

MODULE_A_VERSION = "v1"
MODULE_B_VERSION = "v1"