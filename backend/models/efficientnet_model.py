import timm
import torch.nn as nn


class EfficientNetClassifier(nn.Module):
    def __init__(self, num_classes=4):
        super().__init__()

        self.model = timm.create_model(
            "efficientnet_b0",
            pretrained=True
        )

        in_features = self.model.classifier.in_features

        self.model.classifier = nn.Linear(
            in_features,
            num_classes
        )

    def forward(self, x):
        return self.model(x)