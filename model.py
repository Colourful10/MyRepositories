import timm
import torch
# from fastai.version.all import *

avail_pretrained_models = timm.list_models(pretrained=True)

model = timm.create_model('resnet34', pretrained=True)

print(model)

# torch.randn(1,1,32,32)是batch_size=1, 图像通道数为1,图像尺寸为32x32
print(model.default_cfg)

#here i updated yeah