#Source Code for Mining data on Twitter with Python Course by TigerStyle Code Academy 
# Tweets are stored in "fname"
import json

fname = "C:/Users/Sukhvinder Singh/pythonscripts/MiningSocialMedia/stream___EXITPolls2017___PunjabElections2017_aap.jsonl"
counter = 0
"""
with open(fname, 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if tweet['coordinates']:
            print("Yes!")
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)
 
# Save geo data
with open('new_geo.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4)
"""
with open(fname, 'r') as f:

    for line in f:
        tweet = json.loads(line)
        print(tweet['coordinates'])
        counter += 1
        print (counter)
        if counter == 10:
            break