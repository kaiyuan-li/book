# Deep Dive into Learning

## Recurrent network

### Sequential data processing
```py
T = 1000 # the length of the time sequence
tau = 4 # length of each input data
features = torch.zeros((T - tau, tau)) # each window of 4 is a feature, i.e. input data
# reshape the list of x[tau:] into a tensor that has only 1 element in the second dimension
# -1 means the size of the first dimension will be auto decided
labels = x[tau:].reshape((-1, 1)) 
```

Data loader
```py
def load_array(data_arrays, batch_size, is_train=True):
  dataset = data.TensorDataset(*data_arrays)
  return data.DataLoader(dataset, batch_size, shuffle=is_train)
```

Example of preparing dataset:
```py
import torch
from torch.utils.data import TensorDataset, DataLoader

# Example tensors
features = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
labels = torch.tensor([0, 1, 0], dtype=torch.float32)

# Create a TensorDataset
dataset = TensorDataset(features, labels)

# Create a DataLoader
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Usage
for batch_features, batch_labels in dataloader:
    print(batch_features, batch_labels)
```

Prepare data
```py
batch_size, n_train = 16, 600
# prepare the data into batches of size 16. Each sample is picked from a pool of 600 existing data points
train_iter = load_array((features[:n_train], labels[:n_train]), batch_size, is_train=True)
```

Create the model
```py
import torch.nn as nn

def init_weights(m):
  if type(m) == nn.Linear:
    nn.init.xavier_uniform_(m.weight)

def get_net():
  net = nn.Sequential(nn.Linear(4, 10), nn.ReLU(), nn.Linear(10, 1))
  # applies the function on all modules in the model
  net.apply(init_weights)
  return net

loss_fn = nn.MSELoss(reduction='none')
```

Train the model
```py
def train(net, train_iter, loss, epochs, lr):
  trainer = torch.optim.Adam(net.parameters(), lr)
  for epoch in range(epochs):
    for X, y in train_iter:
      trainer.zero_grad()
      loss = loss_fn(net(X), y)
      loss.sum().backward()
      trainer.step()
    print(f"epoch {epoch}")
    print(f"loss: {d2l.evaluate_loss(net, train_iter, loss):f}")
```

### Text processing

Get text as lines
```
lines = d2l.read_time_machine()
```

Convert lines into tokens
```py
# Creates an array of array. Each row array is the tokens from line.split().
tokens = d2l.tokenize(lines)
```

Create vocabulary, i.e. map tokens into numbers.

```py
# result will be [('<unk>', 0), ('the', 1), ...]
vocab = d2l.Vocab(tokens)
```
### Language models

### Recurrent neural network
