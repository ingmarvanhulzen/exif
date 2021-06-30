#!/usr/bin/python
import argparse
import os
import sys
import piexif

from pathlib import Path
from PIL import Image
from termcolor import colored


OUTPUT_DIR = Path(__file__).parent.absolute() / 'output'


def determine_image(source):
    try:
        Image.open(source)
    except:
        sys.stdout.writelines(
            [
                colored('Error opening source image\n', 'red'),
                colored(f'{source} could not be opend as image\n', 'red'),
            ]
        )
        sys.exit()


def generate(source):
    methods = {
        2: lambda img: img.copy().transpose(0),  # Image.FLIP_LEFT_RIGHT
        3: lambda img: img.copy().transpose(3),  # Image.ROTATE_180
        4: lambda img: img.copy().transpose(1),  # Image.FLIP_TOP_BOTTOM
        5: lambda img: img.copy().transpose(5),  # Image.TRANSPOSE
        6: lambda img: img.copy().transpose(4).rotate(180),  # Image.ROTATE_270
        7: lambda img: img.copy().transpose(6),  # Image.TRANSVERSE
        8: lambda img: img.copy().transpose(2).rotate(180),  # Image.ROTATE_90
    }

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    with Image.open(source) as image:
        exif_dict = piexif.load(source)

        for exif, method in methods.items():
            with open(OUTPUT_DIR / f'exif_{exif}.jpg', mode='w') as fs:
                exif_dict['0th'][274] = exif

                method(image).save(
                    fs,
                    format=image.format,
                    quality=100,
                    subsampling=0,
                    exif=piexif.dump(exif_dict),
                )

                sys.stdout.write(
                    colored(f'Succesfully generated exif orientation {exif}\n', 'cyan')
                )


def main(args):
    if args.input:
        source = str(args.input.absolute())

        determine_image(source)

        generate(source)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        help="source image to generate exif orientations",
        type=Path,
    )

    args = parser.parse_args()

    main(args)
