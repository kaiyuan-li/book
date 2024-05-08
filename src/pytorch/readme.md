# PyTorch

## DataSets and DataLoaders

* `torch.utils.data.Dataset` stores the samples and their corresponding labels
* `torch.utils.data.DataLoader` wraps an iterable around `Dataset`

### Loading a Dataset

Example
```py
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
```


### Iterating and Visualizing the Dataset

```py
labels_map = {
    0: "T-shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()
```

### Creating a Custom Dataset for your files

A custom Dataset class must implement three functions: `__init__`, `__len__`, and `__getitem__`.

```py
import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        """
        returns the number of samples
        """
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        img = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```

`label.csv` file looks like this:
```
tshirt1.jpg, 0
ankleboot999.jpg, 9
```

### Prepare data for training with DataLoaders

`Dataset` retrieves the dataset's features and albels one sample at a time. While training a model, we want to pass samples in "minibatches", reshuffle the data at every epoch to reduce model overfitting, and use python's `multiprocessing` to speed up data retrieval.

```py
from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
```

### Iterate through the `DataLoader`

Data will be shuffled after we iterate over all batches since we specified `shuffle=True`.
```py
# Display image and label. feature = image here.
train_features, train_labels = next(iter(train_dataloader))
print(f"Feature batch shape: {train_features.size()})
print(f"Labels batch shape: {train_labels.size()}")
# first dimension is batch index in the tensor. squeeze() will remove that dimension.
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="gray")
plt.show()
print(f"Label: {label}")
```

## Transforms

In TorchVision datasets, `transform` modifies the features and `target_transform` modifies the label.

The FashionMNIST features are in PIL image format and labels are integers. For training, we need the features as normalized tensors, and the labels as one-hot encoded tensors.

```py
import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = dataset.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)
```
## Build the Neural Network

```py
import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
```


### Get Device for Training
```py
device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
```

### Define the Class
We define our neural network by subclassing `nn.Module`.
```py
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512)
            nn.ReLU()
            nn.Linear(512, 512),
            nn.ReLU()
            nn.Linear(512, 10)
        )
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)
```

To use the model,
```py
X = torch.rand(1, 28, 28, device=device)
# logits is a n x 10 tensor, where n is the sample size of input
logits = model(X)
# softmax maps [-inf, inf] to [0, 1]
pred_prob = nn.Softmax(dim=1)(logits)
# find the max index of each one in the first dim
y_pred = pred_prob.argmax(1)
```

### nn.Flatten
```py
input_image = torch.rand(3, 28, 28)
flatten = nn.Flatten()
flat_image = flatten(input_image)
print(flat_image.size())
# will output torch.Size([3, 784])
```

### nn.Linear
Create a fully connected layer.

### nn.ReLU
Introduces non-linearity, e.g. max(x, 0)



## Optimization
```py
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

train_dataloader = DataLoader(training_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork()
```


### Hyperparams
* Epoch - the number of times to tierate over the dataset
* Batch size - the number of data samples propagated through the network before parameters are updated
* Learning Rate - how much to update models parameters at each batch/epoch

### Optimization Loop

Each iteration of the optimization loop is called an epoch

Each epoch consists of two main parts:
* Train Loop - iterate over training dataset and try to converge to optimal params
* Validation/Test Loop - iterate over test dataset to check of performance is improving

### Loss function
In test loop, we define a loss function to evaluate the accuracy. here we use `nn.CrossEntropyLoss` that combines `nn.Softmax` and `nn.NLLLoss`.

### Optimizer

There are many different optimizers available in pytorch that work better for different kinds of models and data. For example
```py
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
```

Inside the training loop, optimization happens in three steps:
* Call `optimizer.zero_grad()` to reset the gradients of model parameters. By default gradients add up, so we explicitly resets them at each iteration to avoid double counting.
* Backpropagate the prediction loss with a call to `loss.backward()`.
* Once we have our gradients, we call `optimizer.step()` to adjust the parms by gradients collected in the backward pass.

### Full Implementation

```py
def train_loop(data_loader, model, loss_fn, optimizer):
    size = len(data_loader.dataset)
    # set the model into training mode
    model.train()
    for batch, (X, y) in enumerate(data_loader):
        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * batch_size + len(X)
            print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")

def test_loop(dataloader, model, loss_fn):
    # set the model into eval mode
    model.eval()
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
```

## References