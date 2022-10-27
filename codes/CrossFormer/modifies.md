# 记录对于代码的修改以方便Debug

`models\crossformer.py`:

10.27:

讨论完之后决定小数据集和大数据集上同时开始进行实验；

网络的层数设置需要修改，统一改为2，2，18，2的模式；

目标类数设置为200；

再检查一遍代码；

需要跑的实验：

- [ ] 原版crossformer；
- [ ] 原版crossformer换conditional positional encodings;
- [ ] 修改过后的linear pad，3/4为分界线版本crossformer；
- [ ] 修改过后的linear pad，轮替交换版本crossformer；
