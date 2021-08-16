import json
from requests import Session
from requests.adapters import HTTPAdapter
from termcolor import colored


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
saveLocation = "C:/.../" + channelName + \
    "-follows.txt"  # Put the location you'd
metasaveLocation = "C:/.../" + channelName + "-meta.txt"

###################################################################

session = Session()
channelId = ""
channelIdUrl = "https://api.twitch.tv/kraken/users?login=" + channelName

retryAdapter = HTTPAdapter(max_retries=2)
session.mount('https://', retryAdapter)
session.mount('http://', retryAdapter)

# Find the Channel ID
response = session.get(channelIdUrl, headers={
    'Client-ID': clientId,
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Content-Type': 'application/json'
})

result = json.loads(response.text)

print(result)

if result:
    channelId = result["users"][0]["_id"]

print(colored("ChannelID: ", "red"), colored(channelId, "yellow"))

result = None
response = None
offset = 0
limit = 100
subList = []
int_num = offset
direction = "desc"  # asc old, desc new
cursor = ""
f = open(saveLocation, 'w')
mf = open(metasaveLocation, "w")

while True:
    print(colored('Lets check your Followers ', 'green'),
          colored(str(offset), "blue"))

    apiRequestUrl = "https://api.twitch.tv/kraken/channels/" + channelId + "/follows?limit=" + str(
        limit) + "&offset=" + str(offset) + "&cursor=" + cursor + "&direction=" + direction

    # Do the API Lookup
    response = session.get(apiRequestUrl, headers={
        'Client-ID': clientId,
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Authorization': 'OAuth ' + accessToken,
        'Content-Type': 'application/json'
    })

    result = json.loads(response.text)
    print(result)
    _total = result['_total']

    try:
        cursor = result['_cursor']
    except KeyError:
        print(colored("No Cursor left", "green"))
        break

    print(colored("Cursor: ", "red"), colored(cursor, "yellow"))

    if result:
        for sub in result["follows"]:
            # data
            c_display_name = sub['user']['display_name']
            c_id = sub['user']['_id']
            c_name = sub['user']['name']
            c_type = sub['user']['type']
            c_bio = sub['user']['bio']
            c_created_at = sub['user']['created_at']
            c_updated_at = sub['user']['updated_at']
            c_logo = sub['user']['logo']

            c = [c_display_name, c_id, c_name, c_type,
                 c_bio, c_created_at, c_updated_at, c_logo]
            i = 0
            while i < len(c):
                try:
                    mf.write(c[i] + "\n")
                except UnicodeEncodeError:
                    mf.write("Error: 1" + "\n")
                    print(colored(str(i) + " UnicodeError", "red"))
                except TypeError:
                    mf.write("Error: 2" + "\n")
                    print(colored(str(i) + " TypeError", "red"))
                i += 1
            mf.write("\n")

            name = sub['user']['display_name']
            if name != channelName:
                int_num += 1
                print(colored(str(int_num), "blue") + " - " + name)
                try:
                    f.write(name + "\n")
                except ValueError:
                    print(colored(str(int_num) + " - " +
                          name + " isn't writable", "red"))
    else:
        break

f.close()
mf.close()
print("Files Closed")
