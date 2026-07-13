from pathlib import Path

from backend.services.vision_service import VisionService
from backend.services.lifestyle_service import LifestyleService
from backend.services.chatbot_service import chatbot
from backend.services.gradcam_service import GradCAMService

from backend.reports.generate_pdf import PDFReportGenerator


class ReportService:

    def __init__(self):

        self.vision = VisionService()
        self.lifestyle = LifestyleService()
        self.gradcam = GradCAMService()
        self.pdf = PDFReportGenerator()

    def generate_report(self, image_path):

        # ----------------------------
        # Prediction
        # ----------------------------

        prediction = self.vision.analyze_image(image_path)

        disease = prediction["prediction"]

        # ----------------------------
        # Lifestyle
        # ----------------------------

        lifestyle = self.lifestyle.get_recommendations(
            disease
        )

        # ----------------------------
        # AI Summary
        # ----------------------------

        question = f"""
Explain {disease} in simple language.
Include symptoms, causes,
treatment and prevention.
"""

        ai_summary = chatbot.ask(question)

        # ----------------------------
        # GradCAM
        # ----------------------------

        output_folder = Path("outputs")
        output_folder.mkdir(exist_ok=True)

        gradcam_path = output_folder / "report_gradcam.jpg"

        self.gradcam.generate(
            image_path,
            str(gradcam_path)
        )

        # ----------------------------
        # PDF
        # ----------------------------

        pdf_path = output_folder / "Medical_Report.pdf"

        self.pdf.generate(

            output_path=str(pdf_path),

            prediction_result=prediction,

            lifestyle=lifestyle,

            ai_summary=ai_summary,

            eye_image=image_path,

            gradcam_image=str(gradcam_path)

        )

        return {

            "status": "success",

            "report_path": str(pdf_path)

        }