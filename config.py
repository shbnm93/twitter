import pymongo

"""
   Variables that contain user credentials for Twitter API as well as
   client for local MongoDB database.

    Intructions:

    - paste your own Twitter credentials into the empty strings.
    - when finished, save and rename this file as config.py (important!)
"""

### TWITTER CREDENTIALS ###
CONSUMER_API_KEY = "kxmvDSH8ELe4fyodX5DwDovL6"
CONSUMER_API_SECRET = "m5igXnOJMvhJ7DxhT7W1a6LC3A0407DYfc7uEZIXgE16CiXgLM"
ACCESS_TOKEN = "1043409037012992000-eoDC9EP7nNX0K1AHW0f7I4qnZ9eGgA"
ACCESS_TOKEN_SECRET = "22bGSn95wgwf7u49Hs13ZFDfvMbnUI6HVciXV8a13eFKD"

### CONNECTING TO LOCAL MONGODB ###


LOCAL_CLIENT = pymongo.MongoClient("mongodb://istdsa:istdsa@cluster0-shard-00-00.vkg9p.mongodb.net:27017,cluster0-shard-00-01.vkg9p.mongodb.net:27017,cluster0-shard-00-02.vkg9p.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-jd3mvz-shard-0&authSource=admin&retryWrites=true&w=majority")

