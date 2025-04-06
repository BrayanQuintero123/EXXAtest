from PIL import Image
import os
import torch
from torch.utils.data import Dataset
# Dataset personalizado
class ImageFolderNoLabels(Dataset):
    def __init__(self, image_dir, transform=None):
        self.image_dir = image_dir
        self.transform = transform
        self.images = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.images[idx])
        img = Image.open(img_path).convert("L")
        if self.transform:
            img = self.transform(img)
        return img