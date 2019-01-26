# PICAM DARKNET DEMO

## requirements

- python3
- picamera
- pillow
- envparse

- darknet-nnpack
  - https://github.com/digitalbrain79/darknet-nnpack

## prep

### install darknet-nnpack


### config env

make `.env` file in root dir.

```sh
DARKNET_PATH=/home/pi/darknet-nnpack
```


## test

```sh
python3 src/app.py --demo_mode
```