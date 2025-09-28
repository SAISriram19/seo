# API Documentation

Complete reference for the SEO Keyword Research AI Agent API endpoints.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. In production, consider implementing API key authentication.

## Content Type

All requests should use `Content-Type: application/json`

## Rate Limiting

- Default: 60 requests per minute
- Burst limit: 10 concurrent requests
- Configurable via environment variables

## Error Handling

### Error Response Format

```json
{
  "detail": "Error description",
  "status_code": 400,
  "error_type": "validation_error"
}
```

### HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid input |
| 422 | Validation Error - Invalid data format |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error - Server error |

## Endpoints

### 1. Health Check

Check API health status and agent initialization.

**Endpoint**: `GET /api/health`

**Response**:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000000",
  "agent_initialized": true
}
```

**Example**:
```bash
curl -X GET "http://localhost:8000/api/health"
```

---

### 2. Single Keyword Research

Research keywords for a single seed keyword.

**Endpoint**: `POST /api/research`

**Request Body**:
```json
{
  "seed_keyword": "digital marketing",
  "max_keywords": 50,
  "country": "US",
  "include_questions": true,
  "include_long_tail": true
}
```

**Request Parameters**:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `seed_keyword` | string | Yes | - | The primary keyword to research |
| `max_keywords` | integer | No | 50 | Maximum keywords to return (1-100) |
| `country` | string | No | "US" | Target country code (US, GB, CA, AU, IN) |
| `include_questions` | boolean | No | true | Include question-based keywords |
| `include_long_tail` | boolean | No | true | Include long-tail keyword variations |

**Response**:
```json
{
  "seed_keyword": "digital marketing",
  "total_keywords": 50,
  "processing_time": 12.5,
  "timestamp": "2024-01-01T12:00:00.000000",
  "country": "US",
  "keywords": [
    {
      "keyword": "best digital marketing tools",
      "search_volume": 8900,
      "competition_score": 0.65,
      "difficulty": 45,
      "intent": "commercial",
      "cpc_estimate": 3.25,
      "opportunity_score": 78.5,
      "ranking_probability": 0.70,
      "word_count": 4,
      "character_count": 26
    }
  ],
  "metadata": {
    "api_calls": 51,
    "raw_keywords_generated": 100,
    "filters_applied": ["opportunity_score", "relevance", "competition"]
  }
}
```

**Example**:
```bash
curl -X POST "http://localhost:8000/api/research" \
  -H "Content-Type: application/json" \
  -d '{
    "seed_keyword": "digital marketing",
    "max_keywords": 25,
    "country": "US",
    "include_questions": true,
    "include_long_tail": true
  }'
```

---

### 3. Batch Keyword Research

Research keywords for multiple seed keywords simultaneously.

**Endpoint**: `POST /api/batch-research`

**Request Body**:
```json
{
  "seed_keywords": [
    "digital marketing",
    "content strategy",
    "seo optimization"
  ],
  "max_keywords_each": 25,
  "country": "US"
}
```

**Request Parameters**:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `seed_keywords` | array | Yes | - | Array of seed keywords to research |
| `max_keywords_each` | integer | No | 25 | Max keywords per seed keyword |
| `country` | string | No | "US" | Target country code |

**Response**:
```json
{
  "digital marketing": {
    "seed_keyword": "digital marketing",
    "total_keywords": 25,
    "processing_time": 8.2,
    "timestamp": "2024-01-01T12:00:00.000000",
    "country": "US",
    "keywords": [...],
    "metadata": {...}
  },
  "content strategy": {
    "seed_keyword": "content strategy",
    "total_keywords": 25,
    "processing_time": 7.8,
    "keywords": [...],
    "metadata": {...}
  },
  "seo optimization": {
    "error": "Processing failed",
    "seed_keyword": "seo optimization",
    "total_keywords": 0,
    "keywords": []
  }
}
```

**Example**:
```bash
curl -X POST "http://localhost:8000/api/batch-research" \
  -H "Content-Type: application/json" \
  -d '{
    "seed_keywords": ["digital marketing", "content strategy"],
    "max_keywords_each": 15,
    "country": "US"
  }'
```

---

### 4. Export to CSV

Export keyword research results directly to CSV format.

**Endpoint**: `POST /api/export/csv`

**Request Body**: Same as `/api/research`

**Response**: CSV file download

**Headers**:
- `Content-Type: text/csv`
- `Content-Disposition: attachment; filename=keywords_digital_marketing.csv`

**CSV Format**:
```csv
Keyword,Opportunity Score,Search Volume,Competition Score,Difficulty,Intent,CPC Estimate,Ranking Probability
best digital marketing tools,78.5,8900,0.65,45,commercial,3.25,0.70
digital marketing guide,72.3,5400,0.58,38,informational,2.10,0.75
```

**Example**:
```bash
curl -X POST "http://localhost:8000/api/export/csv" \
  -H "Content-Type: application/json" \
  -d '{
    "seed_keyword": "digital marketing",
    "max_keywords": 25
  }' \
  --output keywords.csv
```

---

## Data Models

### Keyword Object

```json
{
  "keyword": "string",                    // The keyword phrase
  "search_volume": "integer",             // Estimated monthly searches
  "competition_score": "float",           // Competition level (0-1)
  "difficulty": "integer",                // Keyword difficulty (1-100)
  "intent": "string",                     // Search intent classification
  "cpc_estimate": "float",                // Estimated cost per click
  "opportunity_score": "float",           // Overall opportunity score (0-100)
  "ranking_probability": "float",         // First-page ranking probability (0-1)
  "word_count": "integer",                // Number of words in keyword
  "character_count": "integer"            // Total character count
}
```

### Search Intent Types

| Intent | Description | Example |
|--------|-------------|---------|
| `informational` | Seeking information/learning | "how to do digital marketing" |
| `commercial` | Researching before purchase | "best digital marketing tools" |
| `transactional` | Ready to buy/take action | "buy digital marketing course" |
| `navigational` | Looking for specific site | "google ads login" |

### Country Codes

Supported country codes for research:

| Code | Country |
|------|---------|
| US | United States |
| GB | United Kingdom |
| CA | Canada |
| AU | Australia |
| IN | India |

## Advanced Usage

### Filtering Results

Use query parameters to filter results:

```bash
# Get only high-opportunity keywords
curl "http://localhost:8000/api/research" \
  -d '{"seed_keyword": "seo", "max_keywords": 100}' | \
  jq '.keywords[] | select(.opportunity_score > 75)'

# Get only commercial intent keywords  
curl "http://localhost:8000/api/research" \
  -d '{"seed_keyword": "marketing"}' | \
  jq '.keywords[] | select(.intent == "commercial")'
```

### Batch Processing with Custom Parameters

```json
{
  "seed_keywords": [
    "digital marketing",
    "social media marketing", 
    "email marketing",
    "content marketing"
  ],
  "max_keywords_each": 20,
  "country": "US"
}
```

### Error Handling Examples

#### Validation Error Response

```json
{
  "detail": [
    {
      "loc": ["body", "seed_keyword"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

#### Rate Limit Error Response

```json
{
  "detail": "Rate limit exceeded. Try again in 60 seconds.",
  "status_code": 429,
  "retry_after": 60
}
```

#### Server Error Response

```json
{
  "detail": "OpenAI API service temporarily unavailable",
  "status_code": 500,
  "error_type": "external_service_error"
}
```

## Response Time Optimization

### Factors Affecting Speed

1. **Number of Keywords**: More keywords = longer processing time
2. **API Rate Limits**: External API response times
3. **Network Latency**: Internet connection quality
4. **Server Load**: Concurrent request processing

### Optimization Tips

1. **Use Batch Processing**: More efficient for multiple keywords
2. **Reduce Max Keywords**: Start with smaller sets (10-25)
3. **Enable Caching**: Set `ENABLE_CACHE=true` in environment
4. **Parallel Requests**: Use concurrent requests when possible

### Performance Benchmarks

| Keywords | Avg Time | API Calls |
|----------|----------|-----------|
| 10 | 3-5s | 11 |
| 25 | 6-10s | 26 |
| 50 | 12-18s | 51 |
| 100 | 25-35s | 101 |

## SDK Examples

### Python SDK Usage

```python
import requests
import json

class SEOAgent:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
    
    def research_keywords(self, seed_keyword, max_keywords=50):
        url = f"{self.base_url}/api/research"
        data = {
            "seed_keyword": seed_keyword,
            "max_keywords": max_keywords
        }
        response = requests.post(url, json=data)
        return response.json()
    
    def batch_research(self, seed_keywords, max_each=25):
        url = f"{self.base_url}/api/batch-research"
        data = {
            "seed_keywords": seed_keywords,
            "max_keywords_each": max_each
        }
        response = requests.post(url, json=data)
        return response.json()

# Usage
agent = SEOAgent()
results = agent.research_keywords("digital marketing", 25)
print(f"Found {results['total_keywords']} keywords")
```

### JavaScript/Node.js SDK Usage

```javascript
class SEOAgent {
  constructor(baseUrl = 'http://localhost:8000') {
    this.baseUrl = baseUrl;
  }

  async researchKeywords(seedKeyword, maxKeywords = 50) {
    const response = await fetch(`${this.baseUrl}/api/research`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        seed_keyword: seedKeyword,
        max_keywords: maxKeywords
      })
    });
    return response.json();
  }

  async batchResearch(seedKeywords, maxEach = 25) {
    const response = await fetch(`${this.baseUrl}/api/batch-research`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        seed_keywords: seedKeywords,
        max_keywords_each: maxEach
      })
    });
    return response.json();
  }
}

// Usage
const agent = new SEOAgent();
agent.researchKeywords('digital marketing', 25)
  .then(results => {
    console.log(`Found ${results.total_keywords} keywords`);
    console.log('Top keyword:', results.keywords[0]);
  });
```

## Webhook Integration

For real-time notifications when research completes:

### Setting Up Webhooks

1. Configure webhook URL in environment:
```env
WEBHOOK_URL=https://your-app.com/api/webhooks/seo
WEBHOOK_SECRET=your-secret-key
```

2. Webhook payload example:
```json
{
  "event": "research_complete",
  "timestamp": "2024-01-01T12:00:00.000000",
  "data": {
    "seed_keyword": "digital marketing",
    "total_keywords": 50,
    "processing_time": 12.5,
    "top_keyword": {
      "keyword": "best digital marketing tools",
      "opportunity_score": 78.5
    }
  },
  "signature": "sha256=abc123..."
}
```

## OpenAPI Specification

The complete OpenAPI/Swagger specification is available at:

```
GET /docs          # Interactive documentation
GET /redoc         # ReDoc documentation  
GET /openapi.json  # Raw OpenAPI spec
```

## Versioning

API versioning is handled through URL paths:

- Current: `/api/research` (v1, default)
- Future: `/api/v2/research` (v2)

## Support

For API-related issues:

1. Check response status codes and error messages
2. Verify request format against examples
3. Test with minimal parameters first
4. Check API health endpoint
5. Review rate limiting settings

---

**Note**: This API is designed for programmatic access to SEO keyword research. For interactive use, consider the web interface at the root URL.