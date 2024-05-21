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
