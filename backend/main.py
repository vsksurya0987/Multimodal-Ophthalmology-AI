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
    allow_origins=["*"],   # Change this back to your frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# LAZY LOAD SERVICES
# =====================================================

vision_service = None
gradcam_service = None
report_service = None
lifestyle_service = None


def get_vision_service():
    global vision_service
    if vision_service is None:
        vision_service = VisionService()
    return vision_service


def get_gradcam_service():
    global gradcam_service
    if gradcam_service is None:
        gradcam_service = GradCAMService()
    return gradcam_service


def get_report_service():
    global report_service
    if report_service is None:
        report_service = ReportService()
    return report_service


def get_lifestyle_service():
    global lifestyle_service
    if lifestyle_service is None:
        lifestyle_service = LifestyleService()
    return lifestyle_service


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

    result = get_vision_service().analyze_image(str(file_path))

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

    return get_lifestyle_service().get_recommendations(disease)


# =====================================================
# GRAD-CAM
# =====================================================

@app.post("/gradcam")
async def generate_gradcam(file: UploadFile = File(...)):

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = OUTPUT_FOLDER / f"gradcam_{file.filename}"

    get_gradcam_service().generate(
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

    result = get_report_service().generate_report(
        str(file_path)
    )

    return FileResponse(
        path=result["report_path"],
        media_type="application/pdf",
        filename="Medical_Report.pdf"
    )