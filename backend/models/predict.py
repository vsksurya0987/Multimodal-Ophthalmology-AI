import torch
from PIL import Image
from torchvision import transforms

from backend.models.load_model import ModelLoader
from config.config import (
    BEST_MODEL,
    IMAGE_SIZE,
    DEVICE
)


class Predictor:

    def __init__(self):

        self.model = ModelLoader().load(BEST_MODEL)

        self.model.to(DEVICE)

        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

        self.class_names = [
            "Normal",
            "Cataract",
            "Glaucoma",
            "AMD"
        ]

    def predict(self, image_path):

        image = Image.open(image_path).convert("RGB")

        image = self.transform(image)

        image = image.unsqueeze(0).to(DEVICE)

        with torch.no_grad():

            outputs = self.model(image)

            probabilities = torch.softmax(outputs, dim=1)

        confidence, prediction = torch.max(probabilities, dim=1)

        top_probabilities, top_indices = torch.topk(probabilities, k=4)

        top_predictions = []

        for prob, idx in zip(top_probabilities[0], top_indices[0]):

            top_predictions.append({

                "disease": self.class_names[idx.item()],

                "confidence": round(prob.item() * 100, 2)

            })

        return {

            "prediction": self.class_names[prediction.item()],

            "confidence": round(confidence.item() * 100, 2),

            "top_predictions": top_predictions

        }