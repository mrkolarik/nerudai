# coding=utf8
import argparse
import os
import json
import io
import re
import shutil

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID";
# The GPU id to use, usually either "0" or "1";
os.environ["CUDA_VISIBLE_DEVICES"] = "0";

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

import numpy as np

from model import build_model, load_weights

from keras.models import Sequential, load_model
from keras.layers import LSTM, Dropout, TimeDistributed, Dense, Activation, Embedding, GRU

DATA_DIR = './data'
MODEL_DIR = './model'

def build_sample_model(vocab_size):
    model = Sequential()
    model.add(Embedding(vocab_size, 512, batch_input_shape=(1, 1), name="embeddingsk"))
    for i in range(3):
        model.add(LSTM(1024, return_sequences=(i != 2), stateful=True, go_backwards=True))
        model.add(Dropout(0.2))

    model.add(Dense(vocab_size, name="densesk"))
    model.add(Activation('softmax'))
    return model

def sample(epoch, header, num_chars):
    with io.open(os.path.join(DATA_DIR, 'char_to_idx.json'), encoding="utf-8") as f:
        char_to_idx = json.load(f)
    idx_to_char = { i: ch for (ch, i) in char_to_idx.items() }
    vocab_size = len(char_to_idx)

    model = build_sample_model(vocab_size)
    load_weights(epoch, model)
    model.save(os.path.join(MODEL_DIR, 'model.{}.h5'.format(epoch)))

    sampled = [char_to_idx[c] for c in header]
    for c in header[:-1]:
        batch = np.zeros((1, 1))
        batch[0, 0] = char_to_idx[c]
        model.predict_on_batch(batch)

    for i in range(num_chars):
        batch = np.zeros((1, 1))
        if sampled:
            batch[0, 0] = sampled[-1]
        else:
            batch[0, 0] = np.random.randint(vocab_size)
        result = model.predict_on_batch(batch).ravel()
        sample = np.random.choice(range(vocab_size), p=result)
        sampled.append(sample)

    basen = ''.join(idx_to_char[c] for c in sampled)
    # regexp_pattern = r".*[A-Z]*\n"
    # # if(header=""):
    #
    # s = StringIO(basen)
    # for line in s:
    #     if (len(line) > 37):
    #         testline = textwrap.fill(line, width=37)
    #         # print(testline)
    #         veta_wrap += testline + "\n"
    #     else:
    #         veta_wrap += line
    # basen_out = re.split(regexp_pattern, basen)[0]
    return basen

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sample some text from the trained model.')
    # parser.add_argument('epoch', type=int, help='epoch checkpoint to sample from')
    parser.add_argument('--seed', default='', help='initial seed for the generated text')
    # parser.add_argument('--len', type=int, default=512, help='number of characters to sample (default 512)')
    args = parser.parse_args()
    #
    # print sample(args.epoch, args.seed, args.len)
    print(sample(80, "ZKUSKA", 2048))
