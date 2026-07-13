import os
import json
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from torch.optim import Adam
from torch.utils.data import DataLoader, random_split
from tqdm import tqdm

from backend.models.vision_dataset import ODIRDataset
from backend.models.efficientnet_model import EfficientNetClassifier

from config.config import (
    DEVICE,
    BATCH_SIZE,
    EPOCHS,
    LEARNING_RATE,
    BEST_MODEL
)


def train():

    print("=" * 60)
    print("Loading Dataset...")
    print("=" * 60)

    dataset = ODIRDataset()

    train_size = int(0.8 * len(dataset))
    valid_size = len(dataset) - train_size

    train_dataset, valid_dataset = random_split(
        dataset,
        [train_size, valid_size],
        generator=torch.Generator().manual_seed(42)
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=0
    )

    valid_loader = DataLoader(
        valid_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=0
    )

    print(f"Training Images   : {len(train_dataset)}")
    print(f"Validation Images : {len(valid_dataset)}")

    #########################################################
    # MODEL
    #########################################################

    model = EfficientNetClassifier()

    model.to(DEVICE)

    criterion = nn.CrossEntropyLoss()

    optimizer = Adam(
        model.parameters(),
        lr=LEARNING_RATE
    )

    #########################################################

    best_accuracy = 0

    history = {
        "train_loss": [],
        "train_accuracy": [],
        "val_accuracy": []
    }

    #########################################################

    for epoch in range(EPOCHS):

        print("\n" + "=" * 60)
        print(f"Epoch {epoch+1}/{EPOCHS}")
        print("=" * 60)

        model.train()

        running_loss = 0

        correct = 0

        total = 0

        loop = tqdm(train_loader)

        for images, labels in loop:

            images = images.to(DEVICE)

            labels = labels.to(DEVICE)

            outputs = model(images)

            loss = criterion(outputs, labels)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

            _, predicted = outputs.max(1)

            total += labels.size(0)

            correct += predicted.eq(labels).sum().item()

            loop.set_postfix(
                loss=loss.item(),
                acc=100 * correct / total
            )

        train_loss = running_loss / len(train_loader)

        train_accuracy = 100 * correct / total

        #########################################################
        # VALIDATION
        #########################################################

        model.eval()

        correct = 0

        total = 0

        with torch.no_grad():

            for images, labels in valid_loader:

                images = images.to(DEVICE)

                labels = labels.to(DEVICE)

                outputs = model(images)

                _, predicted = outputs.max(1)

                total += labels.size(0)

                correct += predicted.eq(labels).sum().item()

        validation_accuracy = 100 * correct / total

        #########################################################

        history["train_loss"].append(train_loss)

        history["train_accuracy"].append(train_accuracy)

        history["val_accuracy"].append(validation_accuracy)

        #########################################################

        print(f"\nTrain Loss      : {train_loss:.4f}")

        print(f"Train Accuracy  : {train_accuracy:.2f}%")

        print(f"Validation Acc. : {validation_accuracy:.2f}%")

        #########################################################

        if validation_accuracy > best_accuracy:

            best_accuracy = validation_accuracy

            torch.save(
                model.state_dict(),
                BEST_MODEL
            )

            print("\nBest Model Saved!")

    #########################################################
    # SAVE HISTORY
    #########################################################

    history_folder = "backend/models/history"

    os.makedirs(history_folder, exist_ok=True)

    with open(
        os.path.join(history_folder, "history.json"),
        "w"
    ) as f:

        json.dump(history, f)

    #########################################################
    # PLOTS
    #########################################################

    plot_folder = "backend/models/plots"

    os.makedirs(plot_folder, exist_ok=True)

    plt.figure(figsize=(8,5))

    plt.plot(history["train_accuracy"], label="Train")

    plt.plot(history["val_accuracy"], label="Validation")

    plt.xlabel("Epoch")

    plt.ylabel("Accuracy")

    plt.title("Training Accuracy")

    plt.legend()

    plt.savefig(
        os.path.join(plot_folder, "accuracy.png")
    )

    plt.close()

    #########################################################

    plt.figure(figsize=(8,5))

    plt.plot(history["train_loss"])

    plt.xlabel("Epoch")

    plt.ylabel("Loss")

    plt.title("Training Loss")

    plt.savefig(
        os.path.join(plot_folder, "loss.png")
    )

    plt.close()

    #########################################################

    print("\n" + "=" * 60)

    print("Training Finished Successfully")

    print(f"Best Validation Accuracy : {best_accuracy:.2f}%")

    print("=" * 60)


if __name__ == "__main__":

    train()