# terralibrary

computers are magic.

screens are horrible.

paper is lovely.

books are beautiful.

*terralibrary is an experiment in creating a library computer that doesn't need a screen.*

## how

- a barcode reader as magic wand
- raspberry pi as brain
- speaker to speak
- receipt printer to print

## inspo

- [Dynamicland](https://dynamicland.org/)
- [ELECTRONICOS FANTASTICOS!](https://www.electronicosfantasticos.com/)

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

Ensure that USB speaker is used by changing speaker in `raspi-config`


