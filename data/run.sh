#!/bin/sh

/ytp/elasticsearch-7.6.0/bin/elasticsearch

if [ -f "/ytp/songs.json" ]
then
    curl -X PUT 'http://localhost:9200/songs?pretty=true'
    curl -X POST 'http://localhost:9200/songs/_mapping' -H 'Content-Type:application/json' -d'{
        "properties": {
            "lyrics": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_smart"
            },
            "singer": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_smart"
            },
            "name": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_smart"
            },
            "date": {
                "type": "keyword",
                "index": true
            }
        }
    }'
    /ytp/upload_data.py
    rm "/ytp/songs.json" "/ytp/upload_data.py"
fi
