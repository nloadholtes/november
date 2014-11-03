#
# pic_flickr.py
#
# Given a picture, upload it to flickr
#
import flickrapi
import sys
import json
import argparse


def main(flickr, files, pic_log):
    for f in files:
        if f not in pic_log:
            print("Uploading %s" % f)
            flickr.upload(filename=f, tags="commit_pics")
            pic_log.append(f)
    with open(sys.argv[1] + ".log", "w") as log:
        log.write(json.dumps(pic_log))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-a', '--apikey', required=True, help="The JSON file detailing our API key")
    ap.add_argument('-f', '--files', nargs="*", required=True, help="The files that can be uploaded")
    args = ap.parse_args()
    jdata = json.load(open(args.apikey))
    pic_log = json.load(open(args.apikey + ".log"))
    api_key = jdata.get("key")
    api_secret = jdata.get("secret")
    flickr = flickrapi.FlickrAPI(api_key, api_secret)
    (token, frob) = flickr.get_token_part_one(perms='write')
    if not token:
        raw_input("Press ENTER after you authorized this program")
    flickr.get_token_part_two((token, frob))
    files = sys.argv[2:]
    main(flickr, args.files, pic_log)
