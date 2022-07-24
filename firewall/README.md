# Source Machine Firewall Requests Log

## Schema

```json
{
  "country": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "d_port": {
    "type": "long"
  },
  "datetime": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "protocol": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "result": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "source_ip": {
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

- Interaction record example

```json
{
  "datetime": "May 27 06:34:53",
  "country": "China",
  "protocol": "TCP",
  "d_port": 445,
  "source_ip": "171.88.165.195",
  "result": "interaction"
}
```

- Scan record example

```json
{
  "datetime": "May 27 06:35:05",
  "country": "Russia",
  "protocol": "TCP",
  "d_port": 5096,
  "source_ip": "45.155.205.41",
  "result": "scan"
}
```
