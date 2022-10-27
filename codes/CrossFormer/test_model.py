import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import torch

from config import _C, _update_config_from_file
from models import build_model

config = _C.clone()
_update_config_from_file(config, 'configs/tiny_patch4_group7_224.yaml')

model = build_model(config, None)
model.cuda()

x = torch.rand((128, 3, 224, 224)).cuda()
out = model(x)

print(out.shape)