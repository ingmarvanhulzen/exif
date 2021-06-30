# Python EXIF oriantation generation script

The following script rotates any giving image and appends given EXIF orientations values.

## Why?

iOS will upload images made with the camera as EXIF orientation 6 (ROTATE_270). To transpose the given image to a web compatible image we use [Pillow](https://github.com/python-pillow/Pillow) and for testing purpose i've created this script to generate all posible variations.

# How to use it?

```bash
python generate.py -i example/original.jpg
```

## Setup

I would recommend to setup a virtual enviorment with [pyenv](https://github.com/pyenv/pyenv) en install the given requirements.txt

```bash
pyenv virtualenv 3.7.3 exif
pyenv activate exif
pip install -r requirements.txt
```
