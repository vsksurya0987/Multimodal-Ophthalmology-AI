from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
from pathlib import Path
from pydantic import BaseModel

from backend.services.vision_service import VisionService
from backend.services.chatbot_service import chatbot
from backend.services.gradcam_service import GradCAMService
from backend.services.report_service import ReportService
from backend.services.lifestyle_service import LifestyleService


app = FastAPI(
    title="Multimodal Ophthalmology AI",
    version="1.0.0"
)

# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# SERVICES
# =====================================================

vision_service = VisionService()
gradcam_service = GradCAMService()
report_service = ReportService()
lifestyle_service = LifestyleService()

# =====================================================
# FOLDERS
# =====================================================

UPLOAD_FOLDER = Path("uploads")
OUTPUT_FOLDER = Path("outputs")

UPLOAD_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)

# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():

    return {
        "message": "Multimodal Ophthalmology AI Backend Running"
    }

# =====================================================
# PREDICT
# =====================================================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = vision_service.analyze_image(str(file_path))

    return result

# =====================================================
# CHATBOT
# =====================================================

class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: ChatRequest):

    answer = chatbot.ask(request.question)

    return {
        "status": "success",
        "question": request.question,
        "answer": answer
    }

# =====================================================
# LIFESTYLE
# =====================================================

@app.get("/lifestyle/{disease}")
def get_lifestyle(disease: str):

    return lifestyle_service.get_recommendations(disease)

# =====================================================
# GRAD-CAM
# =====================================================

@app.post("/gradcam")
async def generate_gradcam(file: UploadFile = File(...)):

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = OUTPUT_FOLDER / f"gradcam_{file.filename}"

    gradcam_service.generate(
        str(file_path),
        str(output_path)
    )

    return FileResponse(
        path=output_path,
        media_type="image/jpeg",
        filename=output_path.name
    )

# =====================================================
# PDF REPORT
# =====================================================

@app.post("/report")
async def generate_report(file: UploadFile = File(...)):

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = report_service.generate_report(
        str(file_path)
    )

    return FileResponse(
        path=result["report_path"],
        media_type="application/pdf",
        filename="Medical_Report.pdf"
    )