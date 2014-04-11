#
# pic_flickr.py
#
# Given a picture, upload it to flickr
#
import flickrapi
import sys
import json


def main(flickr, files):
    print("Files: %s " % files)
    pass


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Need path to the json-formatted api key/secret and then some name(s)")
        exit(-1)
    #Get API key
    jdata = json.load(open(sys.argv[1]))
    api_key = jdata.get("key")
    api_secret = jdata.get("secret")
    print(sys.argv)
    flickr = flickrapi.FlickrAPI(api_key, api_secret)
    files = sys.argv[2:]
    main(flickr, files)
