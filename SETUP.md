## Setup

- Setup a pi according to https://github.com/dantaeyoung/pi-heart/blob/main/README.md


Install pipenv 
- `pip install pipenv`

Install `espeak-ng`
- `sudo apt-get install espeak-ng`

Install modules 
- `pipenv install`
(Use larynx if on a fast enough pi (rpi4))

## USB speaker

Ensure that USB speaker is used by changing speaker in `raspi-config`

## Barcode scanner

Barcode scanner should be one that emulates keyboard input. I'm using a Tera 8100. `python-evdev` is used to grab input. Grab the right device. If it's not working try `testing/evdev_scan.py` to get the right device number and replace code in `main.py`. 

Ideally this should be in a separate config file... but hack first, clean up later!

## PM2

Use PM2 to run

### Install pm2 & run on startup
- `npm install pm2 -g`
- `pm2 startup`

### run terralibrary on pm2
- `pm2 start pm2.yml`
- `pm2 save`
