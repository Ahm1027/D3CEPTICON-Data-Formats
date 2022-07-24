# Dionaea Honeypot Request Logs

### Schema

```json
{
  "connection": {
    "type": "long"
  },
  "connection_timestamp": {
    "type": "float"
  },
  "country": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "download_md5_hash": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "download_url": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "index": {
    "properties": {
      "_index": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      }
    }
  },
  "local_host": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "local_port": {
    "type": "long"
  },
  "remote_host": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "remote_port": {
    "type": "long"
  }
}
```

### Data Sample

```json
{
  "connection": 29628,
  "connection_timestamp": 1651348987.5699076653,
  "local_host": "172.17.0.2",
  "local_port": 445,
  "remote_host": "122.225.80.202",
  "remote_port": 57212,
  "download_url": "",
  "download_md5_hash": "7d58d0c21a1bee604017d732661cfee0",
  "country": "China"
}
```
