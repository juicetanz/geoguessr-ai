# geoguessr-ai

A project intended to determine the location of images, able to be run on a Jetson Nano with the jetson-inference library.

![An example of the model's output](output.jpg)

## Algorithm

The AI is built on the ImageNet image classification model, re-trained with a Geoguessr dataset using resnet-18 and PyTorch.

## Setup

1. SSH into your Nano and clone the [jetson-inference](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo.md) library to it.

2. Download `data/labels.txt`, `models`, and `imagenet.py` to a folder of your choice on your Nano.

3. `cd` into the folder with the console.

4. Run the following command, replacing `[IMAGE PATH]` with the path of the file of your choice:
   `imagenet.py --model=models/resnet18.onnx --labels=data/labels.txt --input_blob=input_0 --output_blob=output_0 [IMAGE PATH] output.jpg`

5. When the command finishes, `output.jpg` will appear in your folder.

[Here is a video demonstration of my project](https://youtu.be/MxcK5CEQdI0)
