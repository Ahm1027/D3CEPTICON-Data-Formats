# Web Honeypot Request Logs

## Schema

```json
{
  "attackerIP": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "datetime": {
    "type": "date"
  },
  "detection": {
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
  "payload": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "port": {
    "type": "long"
  },
  "post_data_1": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "post_data_2": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "type": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  }
}
```

## Data Sample

- Normal request

```json
{
  "payload": "/assets/imgs/team_2.webp",
  "datetime": "2022-05-27T06:34:28.992963",
  "attackerIP": "191.97.60.197",
  "port": 12510,
  "type": "1",
  "post_data_1": null,
  "post_data_2": null,
  "detection": "index"
}
```

- Xss request sample

```json
{
  "payload": "/forms/contact.php",
  "datetime": "2022-05-27T06:34:29.019192",
  "attackerIP": "191.97.60.197",
  "port": 12510,
  "type": "1",
  "post_data_1": "c",
  "post_data_2": null,
  "detection": "xss"
}
```
