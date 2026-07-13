import pandas as pd
from pathlib import Path
from PIL import Image

import torch
from torch.utils.data import Dataset
from torchvision import transforms

from config.config import (
    ANNOTATION_FILE,
    TRAIN_IMAGES,
    IMAGE_SIZE
)

CLASS_COLUMNS = {
    "N": 0,  # Normal
    "C": 1,  # Cataract
    "G": 2,  # Glaucoma
    "A": 3   # AMD
}


class ODIRDataset(Dataset):

    def __init__(self):

        self.df = pd.read_excel(ANNOTATION_FILE)

        self.transform = transforms.Compose([
            transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.485, 0.456, 0.406],
                [0.229, 0.224, 0.225]
            )
        ])

        self.samples = []

        for _, row in self.df.iterrows():

            label = None

            if row["N"] == 1:
                label = 0
            elif row["C"] == 1:
                label = 1
            elif row["G"] == 1:
                label = 2
            elif row["A"] == 1:
                label = 3

            if label is None:
                continue

            left = TRAIN_IMAGES / row["Left-Fundus"]
            right = TRAIN_IMAGES / row["Right-Fundus"]

            if left.exists():
                self.samples.append((left, label))

            if right.exists():
                self.samples.append((right, label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):

        image_path, label = self.samples[idx]

        image = Image.open(image_path).convert("RGB")

        image = self.transform(image)

        return image, torch.tensor(label)