#
# pic_flickr.py
#
# Given a picture, upload it to flickr
#
import flickrapi
import sys


def main(flickr, files):
    pass


if __name__ == '__main__':
    if len(sys.args) > 2:
        print("Need some arguments")
        exit(-1)
    #Get API key
    api_key = sys.argv[1]
    flickr = flickrapi.FlickrAPI(api_key)
    files = []
    main(flickr, files)
