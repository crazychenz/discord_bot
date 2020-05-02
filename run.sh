#!/bin/bash

docker run -ti -v $(pwd):/usr/src/app --rm crazychenz/discord_bot python $@
