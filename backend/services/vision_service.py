from backend.models.predict import Predictor


class VisionService:

    def __init__(self):
        self.predictor = Predictor()

    def analyze_image(self, image_path):

        result = self.predictor.predict(image_path)

        return {
            "status": "success",
            "prediction": result["prediction"],
            "confidence": result["confidence"],
            "top_predictions": result["top_predictions"]
        }