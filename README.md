# Dionaea Honeypot Report Logs for Malwares Captured

### Schema for honeypot

```json
{
  "AntiVirus_bypassed": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "AntiVirus_detected": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "behavior_names": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "behavior_paths": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "collab_ips": {
    "type": "text"
  },
  "hash": {
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
  "package": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "platform": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "score": {
    "type": "long"
  },
  "ttps_data": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "ttps_sequence": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  },
  "type_of_file": {
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

### Data Sample:

```json
{
  "AV_bypassed": [
    "Arcabit",
    "tehtris",
    "F-Secure",
    "CMC",
    "Antiy-AVL",
    "Kingsoft",
    "ZoneAlarm",
    "Acronis",
    "Zoner",
    "Yandex"
  ],
  "AV_detected": [
    "Bkav",
    "Elastic",
    "MicroWorld-eScan",
    "FireEye",
    "CAT-QuickHeal",
    "ALYac",
    "Cylance",
    "Sangfor",
    "K7AntiVirus",
    "Alibaba",
    "K7GW",
    "CrowdStrike",
    "BitDefenderTheta",
    "VirIT",
    "Cyren",
    "Symantec",
    "ESET-NOD32",
    "Baidu",
    "TrendMicro-HouseCall",
    "Paloalto",
    "Cynet",
    "Kaspersky",
    "BitDefender",
    "NANO-Antivirus",
    "SUPERAntiSpyware",
    "Avast",
    "Tencent",
    "Ad-Aware",
    "Comodo",
    "DrWeb",
    "Zillya",
    "TrendMicro",
    "McAfee-GW-Edition",
    "Emsisoft",
    "APEX",
    "Jiangmin",
    "Webroot",
    "Avira",
    "Gridinsoft",
    "Microsoft",
    "ViRobot",
    "GData",
    "SentinelOne",
    "AhnLab-V3",
    "McAfee",
    "TACHYON",
    "VBA32",
    "Malwarebytes",
    "Rising",
    "MAX",
    "MaxSecure",
    "Fortinet",
    "AVG",
    "Panda"
  ],
  "behavior_names": "\"lsass.exe\"",
  "behavior_paths": "\"C:\\\\Windows\\\\System32\\\\lsass.exe\"",
  "hash": "\"6e72ad805b4322612b9c9c7673a45635\"",
  "package": "exe",
  "platform": "windows",
  "score": 10.0,
  "ttps_data": "[{\"T1045\": {\"short\": \"Software Packing\", \"long\": \"Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory.\"}}, {\"T1045\": {\"short\": \"Software Packing\", \"long\": \"Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory.\"}}]",
  "type_of_file": "E x p l o i t : W i n 3 2 / C V E - 2 0 1 7 - 0 1 4 7 . A",
  "ttps_sequence": "[\"T1045\", \"T1045\"]",
  "collab_ips": null,
  "index": null
}
```

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
