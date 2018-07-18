import os
from easydict import EasyDict

cfg = EasyDict()

cfg.net = 'resnet50'
cfg.dataset = 'mnist'

cfg.train_dir = 'train_log'
cfg.batch_size = 30
cfg.w1 = 224
cfg.h1 = 224
cfg.w2 = 28
cfg.h2 = 28
cfg.lmd = 5e-5
cfg.lr = 0.05
cfg.decay = 0.96
cfg.max_epoch = 50

if not os.path.exists(cfg.train_dir):
    os.makedirs(cfg.train_dir)

