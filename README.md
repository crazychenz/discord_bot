# CrazyChenz Thing's Discord Bot

Generate the docker container:
```
pushd docker/discord_bot ; ./build.sh ; popd
```

Inspect the docker container state:
```
./inspect.sh
```

Configure the bot script credentials:
```
echo "DISCORD_TOKEN={TOKEN}" > .env
```

Run a bot script:
```
./run.sh cat.py
```


