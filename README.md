# terralibrary

computers are magic.
screens are horrible.
paper is lovely.
books are beautiful.

terralibrary is an experiment in creating a library computer that doesn't need a screen.

## how

barcode reader
screenless programming + barcode reader + audio = ?


## setup

Install pipenv


~~Install Docker to run Larynx~~
- ~~`sudo apt-get install apt-transport-https ca-certificates software-properties-common -y`~~
- ~~`curl -sSL https://get.docker.com | sh`~~

~~`Install Larynx~~`
- ~~`curl https://raw.githubusercontent.com/rhasspy/larynx/master/docker/larynx-server > larynx-server`~~
- ~~`chmod +755 larynx-server`~~
- ~~move `larynx-server` to somewhere (like `~/bin` or `~/heart/bin`)~~
- ~~`sudo ./larynx-server`~~

Install `espeak-ng`
- `sudo apt-get install espeak-ng`

## USB speaker

Ensure that USB speaker is used
edit `/usr/share/alsa/alsa.conf`
Scroll and find the following two lines:
```
defaults.ctl.card 0
defaults.pcm.card 0
```
Change the 0 to a 1 to match the card number of the USB device :
```
defaults.ctl.card 1
defaults.pcm.card 1
```
