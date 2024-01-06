import torch
from torch.cuda.amp import autocast
from utils import print_color, Colors
import time

def train_epoch(epoch, data_loader, spsa, device, tb_writer):
    start_time = time.time()
    with autocast():
        for _, (images, labels) in enumerate((data_loader)):
            images = images.to(device)
            labels = labels.to(device)
            
            spsa.estimate(epoch, images, labels)
            outputs = spsa.model(images)
            loss = spsa.criterion(outputs, labels)

            correct += (labels == torch.argmax(outputs, dim=1)).float().sum()

    end_time = time.time()

    print_color(f'Training {epoch:2d} | Elapsed Time {end_time - start_time:.3f} | Loss {loss:.5f}', Colors.YELLOW)
