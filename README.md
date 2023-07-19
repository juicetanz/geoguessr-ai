# geoguessr-ai

A project intended to determine the location of images that I made to help me learn the geography of countries.

![An example of the model's output](output.jpg)

## Algorithm

The AI is built on the ImageNet image classification model, re-trained with a Geoguessr dataset using resnet-18 and PyTorch.

## Setup

1. SSH into your Nano and setup the [jetson-inference](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo.md) library.

2. Download and unzip the latest release into a folder of your choice on your Nano.

3. `cd` into the folder with the console.

4. Run the following command, replacing `[IMAGE PATH]` with the path of the file of your choice:
   `python3 imagenet.py --model=resnet18.onnx --labels=labels.txt --input_blob=input_0 --output_blob=output_0 [IMAGE PATH] output.jpg`

5. When the command finishes, `output.jpg` will appear in your folder.

[Here is a video demonstration of my project](https://youtu.be/MxcK5CEQdI0)
