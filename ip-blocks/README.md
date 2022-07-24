# IP Blocks from overall honeypots

## Schema

```json
{
  "I_445": {
    "type": "text"
  },
  "NI_8080": {
    "properties": {
      "crlf": {
        "type": "long"
      },
      "csrf_ssrf_php_injection": {
        "type": "long"
      },
      "index": {
        "type": "long"
      },
      "request_timeline": {
        "properties": {
          "datetime": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
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
          "post_data": {
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
      "sqli": {
        "type": "long"
      },
      "total_requests": {
        "type": "long"
      },
      "wp-content": {
        "type": "long"
      },
      "xss": {
        "type": "long"
      }
    }
  },
  "bot": {
    "type": "boolean"
  },
  "character": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "country": {
    "type": "text"
  },
  "firewall": {
    "properties": {
      "interaction": {
        "type": "long"
      },
      "request_timeline": {
        "properties": {
          "datetime": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "no_of_interactions": {
            "type": "long"
          },
          "no_of_scans": {
            "type": "long"
          }
        }
      },
      "scan": {
        "type": "long"
      }
    }
  },
  "index": {
    "properties": {
      "_id": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
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
  "ip": {
    "type": "text"
  },
  "login_attempts": {
    "type": "object"
  },
  "quote": {
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

```json
{
  "country": "India",
  "ip": "117.194.251.189",
  "bot": false,
  "firewall": {
    "scan": 1,
    "interaction": 0,
    "request_timeline": [
      {
        "datetime": "May 27 06:38:40",
        "no_of_scans": 1,
        "no_of_interactions": 0
      }
    ]
  },
  "I_445": [
    "0ab2aeda90221832167e5127332dd702",
    "20734ce22b624740e115690a84b5d120"
  ],
  "NI_8080": {
    "csrf_ssrf_php_injection": 0,
    "request_timeline": [
      {
        "datetime": "2022-06-16 23:33:56.566760",
        "post_data": null,
        "payload": "/"
      }
    ],
    "wp-content": 0,
    "crlf": 0,
    "total_requests": 1,
    "index": 1,
    "xss": 0,
    "sqli": 0
  },
  "login_attempts": null
}
```
