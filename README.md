# PICAM DARKNET DEMO

## requirements

- python3
- picamera
- pillow
- envparse

- darknet-nnpack
  - https://github.com/digitalbrain79/darknet-nnpack

## prep

### install node.js and tools

- https://kokensha.xyz/raspberry-pi/best-way-to-install-nodejs-to-raspberrypi/

#### install vue cli 3

```sh
$ npm install @vue/cli -g
```

### install darknet-nnpack


### config env

make `.env` file in root dir.

```sh
DARKNET_PATH=/home/pi/darknet-nnpack
```


## test

```sh
python3 app.py --demo_mode
```

## run

### standalone mode

```sh
$ cd frontend
$ npm i
$ npm run build
$ cd ../
$ python3 app.py --server_mode
$ chromium-browser --noerrdialogs --kiosk --incognito http://localhost:8080/
```