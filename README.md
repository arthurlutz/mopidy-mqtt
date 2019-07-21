Based on ![magcode's](https://github.com/magcode) ![work](https://github.com/magcode/mopidy-mqtt).

[![Build Status](https://travis-ci.org/odiroot/mopidy-mqtt.svg?branch=master)](https://travis-ci.org/odiroot/mopidy-mqtt)

# Features

This Mopidy Frontend Extension allows you to control Mopidy with MQTT and retrieve some information from Mopidy via MQTT.
The implementation is very basic. Open for any kind of pull requests.

## Status update

Mopidy sends an update as soon the playback state changes:

`mytopic/state -> 'paused'`

When a new title or stream is started Mopidy sends this via `nowplaying`

`mytopic/nowplaying -> 'myradio'`

## Play a song or stream
You can start playback of a song or stream via MQTT. Send the following:

`mytopic/play -> 'tunein:station:s48720'`

## Stop playback
You can stop the playback via MQTT. Send the following:

`mytopic/control -> 'stop'`

## Change volume
You can change the mixer volume from 0 to 100 via MQTT. Send the following:

`mytopic/volume -> '50'`

# Installation

TODO: Update for the changes.
