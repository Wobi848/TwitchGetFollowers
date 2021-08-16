# TwitchGetFollowers

Little Script to fetch followers from a Twitch Streamer.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
 pip install -r requirements.txt
```

## Usage

```python
##########################################################
#                Configure your stuff here               #
##########################################################
# Twitch API
# Register a Twitch Developer application and put its client ID here
clientId = "YourToken"
# Generate an OAuth token with channel_subscriptions scope and insert your token here
accessToken = "http://localhost"
# Channel Info
channelName = "4wobi"  # Put your channel name here
saveLocation = "C:/.../" + channelName + "-follows.txt"  # Put the location you'd
metasaveLocation = "C:/.../" + channelName + "-meta.txt"

##########################################################
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributors

- [@wobi848](https://github.com/Wobi848/)

## License

[MIT](LICENSE)
