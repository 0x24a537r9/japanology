import requests
import json
from time import sleep
from pprint import pprint

YT = 'https://www.youtube.com/oembed?format=json&url=http://www.youtube.com/watch?v='

handle = open('_data/episodes.json', 'r')
contents = handle.read()
handle.close()

seasons = json.loads(contents)

print('# These episodes are broken:')
for season in seasons:
    for episode in season['episodes']:
        
        # Skip if no vid
        if not episode['vid']:
            continue
        
        # Build url
        path = YT + episode['vid']
        
        # Load
        req = requests.get(path)
        
        isValid = True
        if 'Not Found' in req.content:
            isValid = False
        
            output = '{0}\t{1}\t{2}'.format(episode['title'], episode['date'], episode['vid'])
            print(output)
        
        sleep(1)


