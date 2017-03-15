# resin-playhat-minimal

A minimal resin.io project for the [4tronix PlayHAT](http://4tronix.co.uk/blog/?p=857),
focusing on the buttons and buzzer.

The current setup writes to the log whenever one of the buttons has been
pressed, and when the green button is pressed, the buzzer will sound in
addition to the logs.

This is to demo how to interact with the GPIO buttons, and clarify some of
the information in the [PlayHAT's readme](https://github.com/4tronix/PlayHAT),
for example the correct GPIO pins for some of the buttons.

This project is not using the RGBW LEDs on the board yet.

## License

Copyright 2017 Resinio Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
