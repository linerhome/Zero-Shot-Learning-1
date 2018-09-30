import json
import random

import numpy as np
from scipy.misc import imread, imresize, imsave

from config import *
from utils import *


def main():
    checkpoint = 'BEST_checkpoint.tar'  # model checkpoint
    # Load model
    checkpoint = torch.load(checkpoint)
    model = checkpoint['model']
    model = model.to(device)
    model.eval()

    files = [os.path.join(zsl_a_animals_test_folder, file) for file in os.listdir(zsl_a_animals_test_folder) if
             file.lower().endswith('.jpg')]
    samples = random.sample(files, 10)

    imgs = torch.tensor(10, 3, 224, 224, dtype=torch.float)

    for i, path in enumerate(samples):
        # Read images
        img = imread(path)
        img = imresize(img, (224, 224))
        imsave('images/image_{}.jpg'.format(i), img)

        img = img.transpose(2, 0, 1)
        assert img.shape == (3, 224, 224)
        assert np.max(img) <= 255
        img = torch.FloatTensor(img / 255.)
        imgs[i] = img

    result = []
    preds = model(imgs)
    _, scores = batched_KNN(preds, 1)

    batch_size = preds.size()[0]

    for i in range(batch_size):
        embeded = preds[i]
        print('embeded: ' + str(embeded))
        score = scores[i]
        print('score: ' + str(score))

    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4)


if __name__ == '__main__':
    main()