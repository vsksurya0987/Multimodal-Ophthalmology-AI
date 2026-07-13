from backend.models.predict import Predictor


class VisionService:

    def __init__(self):

        # ==========================================
        # Lazy Loading
        # Do NOT load the AI model when the server starts.
        # It will be loaded only when a prediction request comes.
        # ==========================================

        self.predictor = None

    def load_predictor(self):

        if self.predictor is None:

            print("=" * 60)
            print("Loading EfficientNet-B0 Model...")
            print("=" * 60)

            self.predictor = Predictor()

    def analyze_image(self, image_path):

        # Load the model only on the first prediction
        self.load_predictor()

        result = self.predictor.predict(image_path)

        return {

            "status": "success",

            "prediction": result["prediction"],

            "confidence": result["confidence"],

            "top_predictions": result["top_predictions"]

        }