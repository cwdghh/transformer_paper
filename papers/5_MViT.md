# Multiscale Vision Transformer

> MViT是Facebook AI Research提出的一种视觉Transformer，它借鉴了CNN网络中已有的经验总结，也就是在降低空间分辨率的同时增加通道数，以分别保留高维的语义信息以及低维的细节，具体的做法其实是在Attention之前加上一层卷积；

**Abstract:**

Starting from the input resolution and a small channel dimension, the stages hierarchically expand the channel capacity while reducing the spatial resolution.

Creates a multiscale pyramid of features with early layers operating at high spatial resolution to model simple low-level visual information, and deeper layers at spatially coarse, but complex, high-dimensional features.

## Introduction

Hierarchy of visual processing:

- Reduction in spatial resolution as one goes up the processing hierarchy;
- Increase in the number of different channels, with each channel corresponding to ever more specialized features.

The presence of strong implicit temporal bias in video multiscale models.

## Related Work

**Convolutional networks:** down-sampling, shift invariance, shared weights;

**Self-attention in ConvNets:** 

**Vision Transformers:** build directly a staged model allowing channel expansion and resolution down-sampling. DeiT proposes a data efficient approach to train ViT. A separate line of works attempts at modeling visual data with learnt discretized token sequences.

**Efficient Transformers:** reduce the quadratic attention complexity to make transformers more efficient;

## Multiscale Vision Transformer (MViT)

Builds on the core concept of *stages*;

The main idea of Multiscale  Transformers is to progressively *expand* the channel capacity, while *pooling* the resolution from input to output of the network;

### Multi Head Pooling Attention

MHPA, a self attention operator that enables flexible resolution modeling in a transformer block allowing Multiscale Transformers to operate at progressively changing spatiotemporal resolution;

<img src="./imgs/pooling_attention.png" style="zoom:50%;" />

Consider a $D$ dimensional input tensor $X \in \R^{L \times D}$, then get the intermediate tensors.
$$
\hat{Q} = XW_Q, \ \  \hat{K} = XW_K, \ \ \hat{V} = XW_V
$$
**Pooling Operator:**

Before attending the input, the intermediate tensors are pooled with the pooling operator $\mathcal{P}(\cdot;\Theta)$;

- $\mathcal{P}(\cdot;\Theta)$ performs a pooling kernel computation on the input tensor along each of the dimensions;
- $\Theta := (k, s, p)$, which mean the size of pooling kernel, stride and padding;
- The pooled tensor is flattened again;
- By default use *overlapping* kernels and *shape-preseving* padding, so the output shape has an overall reduction by a factor of $s_Ts_Hs_W$;

**Pooling Attention:**

The pooling operator is applied to all intermediate tensors to get pre-attention vectors $Q, K, V$ with reduced length;

Attention is then computed by
$$
\text{Attention}(Q, K, V) = \text{Softmax}(QK^\top / \sqrt{D})V.
$$
**Multiple Heads:**

$h$ heads where each head is performing the pooling attention on a non-overlapping subset of $D/h$ channels of the $D$ dimensional input tensor $X$.

**Computational Analysis:**

Trade-off between number of channels $D$ and sequence length $L = TWH/f_Qf_K$

### Multiscale Transformer Networks

**Vision Transformer (ViT):**

1. Dicing the input video of resolution $T \times H \times W$, where $T$ is the number of frames, into non-overlapping patches of size $1 \times 16 \times 16$ each;
2. Point-wise application of linear layer on flattened image patches to project them into hidden dimension $D$;
3. A positional emebdding $\bold{E} \in \R^{L \times D}$ is added to each element of the projected sequence of lenght $L$ with dimension $D$ to encode the positional information and break permutation invariance;
4. A learnable class embedding is appended to the projected image patches;
5. The resulting sequence of length $L+1$ is then fed into a stack of $N$ transformer blocks;
6. Sequence after $N$ consecutive blocks is layer-normalizaed and the class embedding is extracted to pass through a linear layer; 

**Multiscale Vision Transformer (MViT):**

Key concept is to progressively *grow the channel* resolution while *reduce the spatiotemporal* resolution;

- **Scale stages:** 
  - a scale stage is defined as a set of $N$ transformer blocks that operate on the same scale. 
  - at the input, we project the patches (or cubes if video) to a smaller channel dimension, but long sequence.
  - at a stage *transition* the channel dimension is up-sampled while the length of the sequence is down-sampled.
- **Channel expansion:** 
  - expand the channel dimension by increasing the output of the final MLP layer;
- **Query pooling:** 
  - affects output length;
  - only the first pooling attention opeator of each stage operates at a non-degenerate stride;
- **Key-Value pooling:** 
- **Skip connections:** 
  - channel dimension and sequence length change inside a residual block;
  - pool the skip connection to adapt to the dimension;

### Network instantiation details

Set the number of MHPA heads to $h = 1$ at the beginning. 

Increase the number of heads with the channel dimension to keep channels per-head remain consistent at 96;

## Experiments: Video Recognition

> 实验部分没有细看；

### Main Results



### Ablations on Kinetics



## Experiments: Image Recognition

### Main Results



## Conclusion

Connect the fundamental concept of multiscale feature hierarchies with the transformer model.