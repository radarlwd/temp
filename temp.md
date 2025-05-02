```
GET your-index/_search
{
  "size": 1000,  // Adjust based on expected results (max 10,000 by default)
  "_source": ["id", "val0", "val1", "val2", "startTime"],  // Fields to include in the table
  "query": {
    "bool": {
      "filter": [
        { "term": { "val0.keyword": "abc" } },
        { "range": { "val1": { "gt": 1, "lt": 100 } } },
        { "term": { "val2": 0 } },
        { 
          "range": { 
            "startTime": { 
              "gte": "now-24h",  // Last 24 hours
              "lt": "now"
            }
          } 
        }
      ]
    }
  },
  "sort": [  // Optional: Sort results by startTime (newest first)
    { "startTime": { "order": "desc" } }
  ]
}
```
