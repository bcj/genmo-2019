# Nano

A collection of [Nano-NaNoGenMo](https://nickm.com/post/2019/11/nano-nanogenmo-or-nnngm/) entries.

## Fragments

Synthesizes a novel by combining like elements between novels by finding blocks of matching characters between the two novels and trying to expand them into words.

### Prerequisites

Novel generation requires Python 3.

This script assumes you have two source novels named `a.txt` and `b.txt`.

### Generation

```bash
python fragments.py > novel.txt
```

## Mask

It combines two novels together using a mask image to decide which source to grab each word from

### Prerequisites

Novel generation requires Python 3.

This script assumes you have two source novels named `a.txt` and `b.txt` and a 24- or 32-bit uncompressed single-image bitmap file named `i.bmp` (make sure your image editor hasn't helpfully created a `png` instead).

### Generation

```bash
python mask.py > novel.txt
```
