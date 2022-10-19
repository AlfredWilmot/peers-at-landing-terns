#!/bin/bash

# install prerequisites if missing (assumes Debian-flavor distro)

if ! dpkg-query -l lynx; then
    sudo apt-get update
    sudo apt-get install -y lynx
fi

# RSS feed (https://en.wikipedia.org/wiki/RSS)
echo "generating 'sample.xml'"
lynx --dump "https://www.sciencedaily.com/rss/top.xml" > sample.xml

# JSON Feed (https://en.wikipedia.org/wiki/JSON_Feed)
echo "generating 'sample.json'"
lynx --dump "https://feeds.npr.org/feeds/1001/feed.json" > sample.json

echo "DONE!"
