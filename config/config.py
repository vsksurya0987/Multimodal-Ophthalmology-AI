from pathlib import Path
import torch

# =====================================================
# PROJECT ROOT
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# =====================================================
# DATASET PATHS
# =====================================================

DATASET_ROOT = PROJECT_ROOT / "datasets"

# ---------------- ODIR ----------------

ODIR_ROOT = DATASET_ROOT / "ODIR"

ODIR_DATASET = ODIR_ROOT / "images" / "ODIR-5K" / "ODIR-5K"

TRAIN_IMAGES = ODIR_DATASET / "Training Images"

TEST_IMAGES = ODIR_DATASET / "Testing Images"

ANNOTATION_FILE = ODIR_DATASET / "data.xlsx"

FULL_DF = ODIR_ROOT / "images" / "full_df.csv"

# ---------------- APTOS ----------------

APTOS_ROOT = DATASET_ROOT / "APTOS"

# ---------------- RFMiD ----------------

RFMID_ROOT = DATASET_ROOT / "RFMiD"

# =====================================================
# MODEL CONFIGURATION
# =====================================================

MODEL_DIR = PROJECT_ROOT / "backend" / "models"

CHECKPOINT_DIR = MODEL_DIR / "checkpoints"

CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

BEST_MODEL = CHECKPOINT_DIR / "best_model.pth"

LAST_MODEL = CHECKPOINT_DIR / "last_model.pth"

MODEL_NAME = "efficientnet_b0"

# =====================================================
# IMAGE CONFIGURATION
# =====================================================

IMAGE_SIZE = 224

BATCH_SIZE = 16

NUM_WORKERS = 0

NUM_CLASSES = 4

CLASS_NAMES = [
    "Normal",
    "Cataract",
    "Glaucoma",
    "Diabetic Retinopathy"
]

# =====================================================
# TRAINING CONFIGURATION
# =====================================================

LEARNING_RATE = 1e-4

WEIGHT_DECAY = 1e-5

EPOCHS = 5

RANDOM_SEED = 42

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# =====================================================
# PATHS
# =====================================================

UPLOAD_FOLDER = PROJECT_ROOT / "uploads"

OUTPUT_FOLDER = PROJECT_ROOT / "outputs"

REPORT_FOLDER = PROJECT_ROOT / "reports"

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# =====================================================
# RAG
# =====================================================

RAG_ROOT = PROJECT_ROOT / "rag"

DOCUMENTS_FOLDER = RAG_ROOT / "documents"

VECTOR_DB_FOLDER = RAG_ROOT / "vectordb"

EMBEDDINGS_FOLDER = RAG_ROOT / "embeddings"

# =====================================================
# SUPABASE
# =====================================================

SUPABASE_URL = ""

SUPABASE_KEY = ""