# Deep Learning With PyTorch

## Basics

Shape of the tensor `torch.tensor([1, 2, 3])` is torch.Size([5])

If we have a batch of images data with shape `[2, 3, 5, 5]`, i.e. batch of 2 images, each image has 3 channels (colored), each image has 5x5 pixels. To apply the weight tensor above to each channel, we have to make the weight tensor above of shape `[3, 1, 1]`.

```py
unsqueezed_weights = weights.unsqueeze(-1).unsqueeze(-1) # will make it [3, 1, 1]
batch_t = torch.randn([2, 3, 5, 5])
batch_weights = (batch_t * unsqueezed_weights)
```

`batch_weights` will have shape of `[2, 3, 5, 5]`. To have two tensors multiplied, align them from the end, each dimension has to match or one of them has to be 1. 1 means always multiply this number. This is called *broadcasting*.

Tensors are saved in `storage`, which is a one dimensional array. To index elements, the storage metadata should have 
1. offset - the first element in global storage.
1. size - shape of the tensor, i.e. how many elements across each dimension the tensor represents
1. stride - the number of elements to skip over to obtain the next element along each dimension.

With stride, the transposing operation don't have to change the storage anymore. Just change the stride since stride changes the order that tensor is serialized. Example:

```py
# shape [3, 4, 5], stride [20, 5, 1]
some_t = torch.ones([3, 4, 5])

# shape [5, 4, 3], stride [1, 5, 20]
transpose_t = some_t.transpose(0, 2)
```

*Contigous* tensor means it's orignal tensor, otherwise (such as transposed) is not contigous. 

Three different types of values
1. continuous
1. ordinal - similar to enum, e.g. large, medium, small
1. categorical - similar to enum too, coffee, milk, soda

Keeping scores as vector of continuous numbers has two implications:
1. smaller numbers are better
1. distance between 1 and 3 is the same distance between 2 and 4.

To create onehot encoding
```py
# create a tensor that has [n_sample, 10 scaled score]
target_onehot = torch.zeros(target.shape[0], 10)

# For each row, take the index of the target label and use it as the column index to set value 1.0
target_onehot.scatter_(1, target.unsqueeze(1), 1.0)
```
In the above example, `target_onehot` is [n x 10], target is [n], target.unsqueeze(1) will give [n x 1]. We can then do scatter([n x 10], [n x 1])

Indexing:
```py
bad_indices = target <= 3
bad_data = data[bad_indices]

mid_data = data[(target > 3) & (target < 7)]
```

This will create a scalar of 1.0: `torch.ones(())`.


Define params with gradient
```py
params = torch.tensor([1.0, 0.0], requires_grad=True) # params.grad will return None

loss = loss_fn(model(t_u, *params), t_c) # now params is used in a loss fn and grad will be populated

params.grad # prints out the gradient
```

Very important **even after calling `backward`, the gradient is not reset. We have to explicitly call `params.grad.zero_()` to reset**.

An example training_loop:
```py
def model(t_u, w, b):
    return w * t_u + b


# tp is predicted temperature.
# tc is actual temperature in celcius
def loss_fn(t_p, t_c):
    squared_diffs = (t_p - t_c) ** 2
    return squared_diffs.mean()


def train_loop(n_epochs, optimizer, params, train_t_u, train_t_c, val_t_u, val_t_c):
    for epoch in range(1, n_epochs + 1):
        train_t_p = model(t_u, *params)
        train_loss = loss_fn(t_p, t_c)

        # don't calculate grad because validation don't need gradient
        with torch.no_grad():
          val_t_p = model(val_t_u, *params)
          val_loss = loss_fn(val_t_p, val_t_c)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if epoch % 500 == 0:
            print(f"epoch {epoch}: loss {loss.item()}")

    return params
```

## Neural network

PyTorch has neurons defined in `torch.nn`. These are subclasses of `nn.Module` and they all have `__call__` method defined.

```py
import torch.nn as nn

linear_model = nn.Linear(1, 1)
linear_model(t_un_val)
```

Even though `linear_model.forward(t_un_val)` can generate the same thing, but do never call `forward()` because `__call__` does a bunch of other things. There are a lot of hooks before and after `forward()`.



## Single Machine Model Parameters ([ref](https://pytorch.org/tutorials/intermediate/model_parallel_tutorial.html))

Model may be too large, split it into multiple GPUs.

After splitting, if we are training in just one batch, GPUs are working on a sequential order so it's still slow.

Divide one batch into multiple splits, calculate the first split on one GPU, then while the second GPU is calculating the first split, the first GPU can calculate the second split.


