import cv2
import numpy as np
import torch

from PIL import Image
from torchvision import transforms

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

from backend.models.load_model import ModelLoader
from config.config import (
    BEST_MODEL,
    IMAGE_SIZE,
    DEVICE
)


class GradCAMService:

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

        # Last convolution layer of EfficientNet-B0
        self.target_layers = [
            self.model.model.conv_head
        ]

    def generate(self, image_path, output_path):

        image = Image.open(image_path).convert("RGB")

        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))

        rgb_image = np.array(image).astype(np.float32) / 255.0

        input_tensor = self.transform(image)

        input_tensor = input_tensor.unsqueeze(0).to(DEVICE)

        cam = GradCAM(
            model=self.model,
            target_layers=self.target_layers
        )

        grayscale_cam = cam(input_tensor=input_tensor)[0]

        visualization = show_cam_on_image(
            rgb_image,
            grayscale_cam,
            use_rgb=True
        )

        visualization = cv2.cvtColor(
            visualization,
            cv2.COLOR_RGB2BGR
        )

        cv2.imwrite(output_path, visualization)

        return output_path