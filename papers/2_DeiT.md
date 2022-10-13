# Training Data-Efficient Image Transformers & Distillation through Attention

> 这是FAIR的一篇工作，目的在于减小Transformer的计算开销，同时介绍了一种针对Transformer的新Teacher-Student策略，可以学习一下如何用相对较少的数据达到良好的效果；

**Abstract:**

Produce competitive convolution-free transformers by training on ImageNet only.

Introduce a teacher-student strategy specific to transformers, which relies on a distillation token ensuring that the student learns from the teacher through attention.

## Introduction

Data-efficient image Transformer, DeiT;

A token-based strategy, advantageously replaces the usual distillation.

Interestingly, with such distillation, image transformers learn more from a ConvNet than from another transformer with comparable performance.

## Related Work

**Knowledge Distillation (KD):** 

the training paradigm in which a *student* model leverages "soft" labels coming from a strong teacher network. This is the output vector of the teacher's softmax function rather than just the maximum of scores, which gives a "hard" label.

It can be regarded as a form of compression of the teacher model into a smaller student model.

## Vision Transformer: Overview

**Multi-head Self Attention layers (MSA):**
$$
\text{Attention}(Q, K, V) = \text{Softmax}(QK^\top/\sqrt d) V,
$$
In self-attention, query, key, and values matrices are themselves computed from a sequence of $N$ input vectors using linear transformations.

In multi-head self-attention (MSA), $h$ self-attention functions are applied to the input.

**Transformer block for images:**

- Add a Feed-Forward Network (FFN) on top of the MSA layer.
- FFN is composed of two linear layers separated by a GeLU activation.
- Both MSA and FFN are operating as residual operators and with a layer normalization.

Add positional embeddings.

**The class token:**



**Fixing the positional encoding across resolutions:**



## Distillation through Attention



## Experiments 

### Transformer Models



### Distillation



### Efficiency vs. Accuracy



## Training Details & Ablation



## Conclusion

