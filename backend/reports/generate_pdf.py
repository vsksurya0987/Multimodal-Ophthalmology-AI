from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

import os
from datetime import datetime


class PDFReportGenerator:

    def generate(
        self,
        output_path,
        prediction_result,
        lifestyle,
        ai_summary,
        eye_image=None,
        gradcam_image=None
    ):

        styles = getSampleStyleSheet()

        doc = SimpleDocTemplate(output_path)

        elements = []

        elements.append(
            Paragraph(
                "<b><font size=18>AI Ophthalmology Medical Report</font></b>",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 0.3 * inch))

        elements.append(
            Paragraph(
                f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 0.2 * inch))

        # --------------------------------------------------

        if eye_image and os.path.exists(eye_image):

            elements.append(
                Paragraph("<b>Uploaded Eye Image</b>", styles["Heading2"])
            )

            elements.append(Image(eye_image, width=3*inch, height=3*inch))

            elements.append(Spacer(1, 0.2 * inch))

        # --------------------------------------------------

        elements.append(
            Paragraph("<b>Prediction Result</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(
                f"Disease : {prediction_result['prediction']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Confidence : {prediction_result['confidence']}%",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 0.2 * inch))

        # --------------------------------------------------

        elements.append(
            Paragraph("<b>Top Predictions</b>", styles["Heading2"])
        )

        for item in prediction_result["top_predictions"]:

            elements.append(
                Paragraph(
                    f"{item['disease']} : {item['confidence']}%",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1, 0.2 * inch))

        # --------------------------------------------------

        elements.append(
            Paragraph("<b>Lifestyle Recommendations</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(
                lifestyle["about"],
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 0.1 * inch))

        elements.append(
            Paragraph("<b>Diet</b>", styles["Heading3"])
        )

        for item in lifestyle["diet"]:
            elements.append(Paragraph(f"• {item}", styles["Normal"]))

        elements.append(Spacer(1, 0.1 * inch))

        elements.append(
            Paragraph("<b>Exercise</b>", styles["Heading3"])
        )

        for item in lifestyle["exercise"]:
            elements.append(Paragraph(f"• {item}", styles["Normal"]))

        elements.append(Spacer(1, 0.1 * inch))

        elements.append(
            Paragraph("<b>Eye Care</b>", styles["Heading3"])
        )

        for item in lifestyle["eye_care"]:
            elements.append(Paragraph(f"• {item}", styles["Normal"]))

        elements.append(Spacer(1, 0.1 * inch))

        elements.append(
            Paragraph("<b>Avoid</b>", styles["Heading3"])
        )

        for item in lifestyle["avoid"]:
            elements.append(Paragraph(f"• {item}", styles["Normal"]))

        elements.append(Spacer(1, 0.3 * inch))

        # --------------------------------------------------

        if gradcam_image and os.path.exists(gradcam_image):

            elements.append(
                Paragraph("<b>Grad-CAM Heatmap</b>", styles["Heading2"])
            )

            elements.append(Image(
                gradcam_image,
                width=3*inch,
                height=3*inch
            ))

            elements.append(Spacer(1, 0.2 * inch))

        # --------------------------------------------------

        elements.append(
            Paragraph("<b>AI Medical Summary</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(
                ai_summary.replace("\n", "<br/>"),
                styles["Normal"]
            )
        )

        doc.build(elements)

        return output_path