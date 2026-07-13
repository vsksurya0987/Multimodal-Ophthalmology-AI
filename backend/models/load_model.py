import torch

from backend.models.efficientnet_model import EfficientNetClassifier
from config.config import DEVICE


class ModelLoader:

    def __init__(self):

        self.device = DEVICE

        self.model = EfficientNetClassifier()

    def load(self, model_path):

        checkpoint = torch.load(
            model_path,
            map_location=self.device
        )

        self.model.load_state_dict(checkpoint)

        self.model.to(self.device)

        self.model.eval()

        return self.model