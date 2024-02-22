# Tesseract Custom Font
This repo is heavily inspired by Gabriel Garcia's [Tesseract Tutorial](https://github.com/astutejoe/tesseract_tutorial)

I recreated it to get a better understanding of how tesstrain works. I've also included [training.sh](./training.sh) to help with the training.

When creating this project, I trained a model to recognize the [Minecraft font](https://github.com/IdreesInc/Minecraft-Font), on top of the English one, hence why the `MODEL_NAME` in [training.sh](./training.sh) is `mc`.

## Usage
**Make sure you clone [tesseract](https://github.com/tesseract-ocr/tesseract) and [tesstrain](https://github.com/tesseract-ocr/tesstrain) before running the code**

If you want to train a model on top op E.G the English one, you need to place the model from the [tessdata repository](https://github.com/tesseract-ocr/tessdata) into tesseract/tessdata.

### Training text
Here you can either use langdata from Tesseract's [langdata repository](https://github.com/tesseract-ocr/langdata), or you can use [generate-training-text.py](./generate-training-text.py), which takes in a list of symbols, and generates random text with it.

### Ground truth
Run [generate-ground-truth.py](./generate-ground-truth.py) and follow instructions given in the terminal. The code uses the `training_text` file in the [data](./data) folder.

### Training
**If you're on windows, you may need to use WSL.**

Use the [training.sh](./training.sh) file and adjust it to your needs. The most important variable to change here is the `MODEL_NAME`.
