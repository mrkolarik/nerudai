# -*- coding: utf-8 -*-
import os
import json
import argparse
from importlib import reload
import sys
reload(sys)
# sys.setdefaultencoding('utf8')
import io
import shutil

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID";
# The GPU id to use, usually either "0" or "1";
os.environ["CUDA_VISIBLE_DEVICES"] = "1";


import numpy as np

from model import build_model, save_weights, load_weights

DATA_DIR = './data'
LOG_DIR = './logs'

BATCH_SIZE = 128
SEQ_LENGTH = 128

class TrainLogger(object):
    def __init__(self, file):
        self.file = os.path.join(LOG_DIR, file)
        self.epochs = 0
        with open(self.file, 'w') as f:
            f.write('epoch,loss,acc\n')

    def add_entry(self, loss, acc):
        self.epochs += 1
        s = '{},{},{}\n'.format(self.epochs, loss, acc)
        with open(self.file, 'a') as f:
            f.write(s)

def read_batches(T, vocab_size):
    length = T.shape[0]
    batch_chars = length // BATCH_SIZE

    for start in range(0, batch_chars - SEQ_LENGTH, SEQ_LENGTH):
        X = np.zeros((BATCH_SIZE, SEQ_LENGTH))
        Y = np.zeros((BATCH_SIZE, SEQ_LENGTH, vocab_size))
        for batch_idx in range(0, BATCH_SIZE):
            for i in range(0, SEQ_LENGTH):
                X[batch_idx, i] = T[batch_chars * batch_idx + start + i]
                Y[batch_idx, i, T[batch_chars * batch_idx + start + i + 1]] = 1
        yield X, Y

def train(text):
    char_to_idx = { ch: i for (i, ch) in enumerate(sorted(list(set(text))))}
    with open(os.path.join(DATA_DIR, 'char_to_idx.json'), 'w') as f:
        data = json.dumps(char_to_idx, ensure_ascii=False)
        f.write(data)

    # idx_to_char = { i: ch for (ch, i) in char_to_idx.items() }
    vocab_size = len(char_to_idx)
    print(vocab_size)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Train the model on some text.')
    # parser.add_argument('--input', default='input.txt', help='name of the text file to train from')
    # parser.add_argument('--epochs', type=int, default=150, help='number of epochs to train for')
    # parser.add_argument('--freq', type=int, default=5, help='checkpoint save frequency')
    # args = parser.parse_args()

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    train(open(os.path.join(DATA_DIR, 'aplhabet.txt')).read())
