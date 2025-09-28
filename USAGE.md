# Usage Guide

Comprehensive guide for using the SEO Keyword Research AI Agent effectively.

## Quick Start

### 1. Basic Web Interface Usage

1. **Start the application**:
   ```bash
   python web_server.py
   ```

2. **Open your browser** to `http://localhost:8000`

3. **Enter a seed keyword** (e.g., "digital marketing")

4. **Configure options**:
   - Set maximum keywords (25-100)
   - Choose target country
   - Toggle question-based keywords
   - Toggle long-tail variations

5. **Click "Research Keywords"** and wait for results

6. **Export results** in CSV or JSON format

### 2. Command Line Interface

```bash
python seo_agent_pro.py
```

Follow the interactive prompts:
- Choose single or batch research
- Enter seed keywords
- Set parameters
- Export results

## Web Interface Guide

### Main Features

#### Research Form
- **Seed Keyword**: Your primary target keyword
- **Max Keywords**: Number of results (25-100 recommended)
- **Target Country**: Geographic focus for search volume data
- **Include Questions**: Adds "how to", "what is" variations
- **Include Long-tail**: Adds 3+ word keyword phrases

#### Results Dashboard
- **Summary Stats**: Overview of research session
- **Keyword Cards**: Detailed metrics for each keyword
- **Sorting**: Results ranked by opportunity score
- **Export Options**: Download as CSV or JSON

#### Keyword Metrics Explained

Each keyword shows:
- **Opportunity Score** (0-100): Overall ranking potential
- **Search Volume**: Estimated monthly searches
- **Competition**: Difficulty level (Easy/Medium/Hard)
- **Intent**: Search purpose (informational, commercial, etc.)
- **CPC Estimate**: Potential advertising cost
- **Ranking Probability**: Likelihood of first-page ranking

### Advanced Web Usage

#### Custom Parameters
Use URL parameters for quick access:
```
http://localhost:8000/?seed=digital%20marketing&max=25&country=US
```

#### Bookmarking Results
Results include shareable URLs with parameters:
```
http://localhost:8000/results?id=research_12345
```

## Command Line Usage

### Single Keyword Research

```bash
python seo_agent_pro.py
# Select option 1
# Enter: digital marketing
# Max keywords: 50
```

**Expected Output**:
```
Starting professional keyword research for: 'digital marketing'
Generating keywords with GPT-4...
Generated 95 keywords from AI
Collecting SEO metrics...
Research complete! 50 keywords in 12.3s

Results for 'digital marketing'
Found 50 keywords in 12.3s
API calls: 51

Top Keywords:
 1. best digital marketing tools      Score:  78.5 | Volume:  8,900 | Comp: 0.65 | Intent: commercial
 2. digital marketing guide           Score:  72.3 | Volume:  5,400 | Comp: 0.58 | Intent: informational
 3. how to do digital marketing       Score:  69.8 | Volume:  3,200 | Comp: 0.52 | Intent: informational
```

### Batch Keyword Research

```bash
python seo_agent_pro.py
# Select option 2
# Enter: digital marketing, content strategy, seo optimization
# Max keywords each: 25
```

**Expected Output**:
```
Batch Keyword Research
Starting batch research for 3 keywords

[1/3] Processing: digital marketing
[2/3] Processing: content strategy  
[3/3] Processing: seo optimization

Batch Results Summary
[+] digital marketing: 25 keywords
[+] content strategy: 25 keywords
[+] seo optimization: 25 keywords

Total keywords generated: 75
Batch research complete in 28.7s
```

## API Usage Examples

### Python Examples

#### Basic Research
```python
import requests

def research_keyword(seed, max_keywords=50):
    url = "http://localhost:8000/api/research"
    data = {
        "seed_keyword": seed,
        "max_keywords": max_keywords,
        "country": "US"
    }
    response = requests.post(url, json=data)
    return response.json()

# Usage
results = research_keyword("digital marketing", 25)
print(f"Found {results['total_keywords']} keywords")

# Display top 5 keywords
for i, kw in enumerate(results['keywords'][:5], 1):
    print(f"{i}. {kw['keyword']} - Score: {kw['opportunity_score']}")
```

#### Batch Processing
```python
import requests
import time

def batch_research(keywords, max_each=25):
    url = "http://localhost:8000/api/batch-research"
    data = {
        "seed_keywords": keywords,
        "max_keywords_each": max_each
    }
    response = requests.post(url, json=data)
    return response.json()

# Usage
seeds = ["digital marketing", "content strategy", "social media"]
results = batch_research(seeds, 20)

for seed, data in results.items():
    if 'error' not in data:
        print(f"{seed}: {data['total_keywords']} keywords")
    else:
        print(f"{seed}: Error - {data['error']}")
```

#### CSV Export
```python
import requests

def export_to_csv(seed_keyword, filename=None):
    url = "http://localhost:8000/api/export/csv"
    data = {
        "seed_keyword": seed_keyword,
        "max_keywords": 50
    }
    
    response = requests.post(url, json=data)
    
    if filename is None:
        filename = f"keywords_{seed_keyword.replace(' ', '_')}.csv"
    
    with open(filename, 'wb') as f:
        f.write(response.content)
    
    print(f"Exported to {filename}")

# Usage
export_to_csv("digital marketing")
```

### JavaScript Examples

#### Browser Usage
```html
<!DOCTYPE html>
<html>
<head>
    <title>SEO Keyword Research</title>
</head>
<body>
    <script>
    async function researchKeywords(seedKeyword) {
        const response = await fetch('http://localhost:8000/api/research', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                seed_keyword: seedKeyword,
                max_keywords: 25
            })
        });
        
        const data = await response.json();
        console.log(`Found ${data.total_keywords} keywords`);
        return data;
    }
    
    // Usage
    researchKeywords('digital marketing')
        .then(results => {
            console.log('Top keyword:', results.keywords[0]);
        });
    </script>
</body>
</html>
```

#### Node.js Usage
```javascript
const fetch = require('node-fetch');

class SEOClient {
    constructor(baseUrl = 'http://localhost:8000') {
        this.baseUrl = baseUrl;
    }

    async research(seedKeyword, options = {}) {
        const url = `${this.baseUrl}/api/research`;
        const data = {
            seed_keyword: seedKeyword,
            max_keywords: options.maxKeywords || 50,
            country: options.country || 'US',
            include_questions: options.includeQuestions !== false,
            include_long_tail: options.includeLongTail !== false
        };

        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        return response.json();
    }

    async batchResearch(seedKeywords, maxEach = 25) {
        const url = `${this.baseUrl}/api/batch-research`;
        const data = {
            seed_keywords: seedKeywords,
            max_keywords_each: maxEach
        };

        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        return response.json();
    }
}

// Usage
const client = new SEOClient();

async function example() {
    try {
        // Single keyword research
        const results = await client.research('digital marketing', {
            maxKeywords: 25,
            country: 'US'
        });
        
        console.log(`Found ${results.total_keywords} keywords`);
        console.log('Top 5 keywords:');
        
        results.keywords.slice(0, 5).forEach((kw, i) => {
            console.log(`${i+1}. ${kw.keyword} (Score: ${kw.opportunity_score})`);
        });
        
        // Batch research
        const batchResults = await client.batchResearch([
            'content marketing',
            'email marketing',
            'social media marketing'
        ], 15);
        
        Object.entries(batchResults).forEach(([seed, data]) => {
            console.log(`${seed}: ${data.total_keywords || 0} keywords`);
        });
        
    } catch (error) {
        console.error('Error:', error);
    }
}

example();
```

## Advanced Usage Scenarios

### 1. Content Planning Workflow

```python
# Research multiple related topics
topics = [
    "content marketing strategy",
    "blog writing tips", 
    "social media content",
    "video marketing",
    "email marketing"
]

results = batch_research(topics, 20)

# Collect all keywords and sort by opportunity
all_keywords = []
for topic, data in results.items():
    if 'keywords' in data:
        for kw in data['keywords']:
            kw['source_topic'] = topic
            all_keywords.append(kw)

# Sort by opportunity score
all_keywords.sort(key=lambda x: x['opportunity_score'], reverse=True)

# Group by intent
by_intent = {}
for kw in all_keywords[:50]:
    intent = kw['intent']
    if intent not in by_intent:
        by_intent[intent] = []
    by_intent[intent].append(kw)

# Create content calendar
print("Content Calendar Based on Keyword Research:")
print("\nWeek 1-2: Commercial Content (Product/Service Focus)")
for kw in by_intent.get('commercial', [])[:5]:
    print(f"- {kw['keyword']} (Volume: {kw['search_volume']:,})")

print("\nWeek 3-4: Informational Content (Educational Focus)")  
for kw in by_intent.get('informational', [])[:5]:
    print(f"- {kw['keyword']} (Volume: {kw['search_volume']:,})")
```

### 2. Competitor Analysis

```python
# Research competitor-focused keywords
competitor_seeds = [
    "best [competitor] alternatives",
    "[your_product] vs [competitor]",
    "[competitor] review",
    "[competitor] pricing"
]

# Replace placeholders with actual names
competitors = ["hubspot", "mailchimp", "canva"]
your_product = "your_saas_tool"

comparison_keywords = []
for competitor in competitors:
    for template in competitor_seeds:
        seed = template.replace("[competitor]", competitor).replace("[your_product]", your_product)
        try:
            result = research_keyword(seed, 10)
            comparison_keywords.extend(result['keywords'])
        except:
            continue

# Sort by ranking probability (easier wins)
comparison_keywords.sort(key=lambda x: x['ranking_probability'], reverse=True)

print("Top Competitor Keyword Opportunities:")
for kw in comparison_keywords[:10]:
    print(f"{kw['keyword']} - Rank Prob: {kw['ranking_probability']:.0%}, Volume: {kw['search_volume']:,}")
```

### 3. Local SEO Research

```python
# Research location-based keywords
base_service = "digital marketing"
locations = ["new york", "los angeles", "chicago", "houston", "miami"]

local_keywords = []
for location in locations:
    seeds = [
        f"{base_service} {location}",
        f"{base_service} services {location}",
        f"{base_service} agency {location}",
        f"{base_service} company {location}",
        f"best {base_service} {location}"
    ]
    
    batch_result = batch_research(seeds, 10)
    
    for seed, data in batch_result.items():
        if 'keywords' in data:
            for kw in data['keywords']:
                kw['target_location'] = location
                local_keywords.append(kw)

# Group by location and find top opportunities
by_location = {}
for kw in local_keywords:
    loc = kw['target_location']
    if loc not in by_location:
        by_location[loc] = []
    by_location[loc].append(kw)

print("Local SEO Opportunities by City:")
for location, keywords in by_location.items():
    # Sort by opportunity score
    keywords.sort(key=lambda x: x['opportunity_score'], reverse=True)
    print(f"\n{location.title()}:")
    for kw in keywords[:3]:
        print(f"  {kw['keyword']} - Score: {kw['opportunity_score']:.1f}")
```

### 4. Seasonal Content Planning

```python
import datetime

# Research seasonal keywords
current_month = datetime.datetime.now().month
seasons = {
    (12, 1, 2): "winter",
    (3, 4, 5): "spring", 
    (6, 7, 8): "summer",
    (9, 10, 11): "fall"
}

# Find current season
current_season = None
for months, season in seasons.items():
    if current_month in months:
        current_season = season
        break

# Research seasonal keywords
base_keyword = "fitness"
seasonal_modifiers = {
    "winter": ["indoor", "home workout", "holiday fitness", "new year"],
    "spring": ["outdoor", "running", "bike", "hiking"],
    "summer": ["beach body", "swimming", "vacation fitness", "hot weather workout"],
    "fall": ["back to school", "marathon training", "gym", "indoor fitness"]
}

if current_season:
    modifiers = seasonal_modifiers[current_season]
    seasonal_seeds = []
    
    for modifier in modifiers:
        seasonal_seeds.extend([
            f"{modifier} {base_keyword}",
            f"{base_keyword} {modifier}",
            f"best {modifier} {base_keyword}"
        ])
    
    seasonal_results = batch_research(seasonal_seeds, 15)
    
    # Collect and sort seasonal keywords
    seasonal_keywords = []
    for seed, data in seasonal_results.items():
        if 'keywords' in data:
            seasonal_keywords.extend(data['keywords'])
    
    seasonal_keywords.sort(key=lambda x: x['opportunity_score'], reverse=True)
    
    print(f"Top {current_season.title()} Content Opportunities:")
    for i, kw in enumerate(seasonal_keywords[:10], 1):
        print(f"{i:2d}. {kw['keyword']:<35} Score: {kw['opportunity_score']:5.1f}")
```

## Integration Examples

### 1. WordPress Integration

```php
<?php
// WordPress plugin integration example

function seo_research_keyword($seed_keyword, $max_keywords = 25) {
    $api_url = 'http://localhost:8000/api/research';
    
    $data = array(
        'seed_keyword' => $seed_keyword,
        'max_keywords' => $max_keywords,
        'country' => 'US'
    );
    
    $response = wp_remote_post($api_url, array(
        'headers' => array('Content-Type' => 'application/json'),
        'body' => json_encode($data),
        'timeout' => 60
    ));
    
    if (is_wp_error($response)) {
        return false;
    }
    
    $body = wp_remote_retrieve_body($response);
    return json_decode($body, true);
}

// Usage in WordPress
function add_keyword_research_metabox() {
    add_meta_box(
        'seo-keyword-research',
        'SEO Keyword Research',
        'seo_keyword_research_callback',
        'post'
    );
}
add_action('add_meta_boxes', 'add_keyword_research_metabox');

function seo_keyword_research_callback($post) {
    $post_title = get_the_title($post->ID);
    
    if ($post_title) {
        $keywords = seo_research_keyword($post_title, 10);
        
        if ($keywords && isset($keywords['keywords'])) {
            echo '<h4>Suggested Keywords for: ' . esc_html($post_title) . '</h4>';
            echo '<ul>';
            foreach ($keywords['keywords'] as $kw) {
                echo '<li>' . esc_html($kw['keyword']) . ' (Score: ' . $kw['opportunity_score'] . ')</li>';
            }
            echo '</ul>';
        }
    }
}
?>
```

### 2. Google Sheets Integration

```javascript
// Google Apps Script integration
function researchKeywordsToSheets() {
    const sheet = SpreadsheetApp.getActiveSheet();
    const seedKeyword = sheet.getRange('A1').getValue();
    
    if (!seedKeyword) {
        Browser.msgBox('Please enter a seed keyword in cell A1');
        return;
    }
    
    const apiUrl = 'http://localhost:8000/api/research';
    const payload = {
        'seed_keyword': seedKeyword,
        'max_keywords': 50,
        'country': 'US'
    };
    
    const options = {
        'method': 'POST',
        'contentType': 'application/json',
        'payload': JSON.stringify(payload)
    };
    
    try {
        const response = UrlFetchApp.fetch(apiUrl, options);
        const data = JSON.parse(response.getContentText());
        
        // Clear previous results
        sheet.getRange('A3:J1000').clear();
        
        // Add headers
        const headers = [
            'Keyword', 'Opportunity Score', 'Search Volume', 
            'Competition', 'Difficulty', 'Intent', 
            'CPC Estimate', 'Ranking Probability', 'Word Count'
        ];
        sheet.getRange(3, 1, 1, headers.length).setValues([headers]);
        
        // Add keyword data
        const keywordData = [];
        data.keywords.forEach(kw => {
            keywordData.push([
                kw.keyword,
                kw.opportunity_score,
                kw.search_volume,
                kw.competition_score,
                kw.difficulty,
                kw.intent,
                kw.cpc_estimate,
                kw.ranking_probability,
                kw.word_count
            ]);
        });
        
        if (keywordData.length > 0) {
            sheet.getRange(4, 1, keywordData.length, headers.length)
                 .setValues(keywordData);
        }
        
        Browser.msgBox(`Research complete! Found ${data.total_keywords} keywords.`);
        
    } catch (error) {
        Browser.msgBox('Error: ' + error.toString());
    }
}
```

## N8N Workflow Usage

### Setting Up the Workflow

1. **Import the workflow**:
   - Copy `n8n-workflow.json` content
   - Import into your N8N instance

2. **Configure nodes**:
   - Update API endpoints if not running on localhost
   - Set up email credentials for reports
   - Configure Slack webhook URL
   - Add Google Sheets credentials

3. **Customize triggers**:
   - Schedule: Run daily/weekly keyword research
   - Webhook: Trigger from external systems
   - Manual: On-demand execution

### Workflow Input Examples

#### Single Keyword Research
```json
{
  "seed_keyword": "digital marketing",
  "max_keywords": 50,
  "country": "US",
  "mode": "single"
}
```

#### Batch Processing
```json
{
  "seed_keywords": [
    "content marketing",
    "social media marketing", 
    "email marketing"
  ],
  "max_keywords_each": 25,
  "country": "US",
  "mode": "batch"
}
```

### Custom N8N Nodes

You can create custom nodes for specific use cases:

```javascript
// Custom node for competitor analysis
const competitorAnalysis = {
  displayName: 'SEO Competitor Analysis',
  name: 'seoCompetitorAnalysis',
  group: ['transform'],
  version: 1,
  
  inputs: ['main'],
  outputs: ['main'],
  
  properties: [
    {
      displayName: 'Competitor Names',
      name: 'competitors',
      type: 'string',
      default: '',
      required: true,
      description: 'Comma-separated list of competitor names'
    },
    {
      displayName: 'Your Product',
      name: 'yourProduct', 
      type: 'string',
      default: '',
      required: true
    }
  ],
  
  async execute() {
    // Implementation for competitor keyword research
    // Returns competitor-focused keywords
  }
};
```

## Performance Optimization Tips

### 1. Batch Processing
- Use batch endpoints for multiple keywords
- Process 3-5 keywords per batch for optimal speed
- Add delays between batches to respect rate limits

### 2. Caching Results
```python
import json
import hashlib
import os
from datetime import datetime, timedelta

class KeywordCache:
    def __init__(self, cache_dir="keyword_cache", ttl_hours=24):
        self.cache_dir = cache_dir
        self.ttl = timedelta(hours=ttl_hours)
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_key(self, seed_keyword, params):
        # Create unique cache key
        cache_data = f"{seed_keyword}_{json.dumps(sorted(params.items()))}"
        return hashlib.md5(cache_data.encode()).hexdigest()
    
    def get(self, seed_keyword, params):
        cache_key = self._get_cache_key(seed_keyword, params)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        if os.path.exists(cache_file):
            # Check if cache is still valid
            file_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
            if datetime.now() - file_time < self.ttl:
                with open(cache_file, 'r') as f:
                    return json.load(f)
        
        return None
    
    def set(self, seed_keyword, params, data):
        cache_key = self._get_cache_key(seed_keyword, params)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        with open(cache_file, 'w') as f:
            json.dump(data, f)

# Usage
cache = KeywordCache()

def cached_research(seed_keyword, **params):
    # Check cache first
    cached_result = cache.get(seed_keyword, params)
    if cached_result:
        print("Using cached results")
        return cached_result
    
    # Research and cache
    result = research_keyword(seed_keyword, **params)
    cache.set(seed_keyword, params, result)
    return result
```

### 3. Parallel Processing
```python
import asyncio
import aiohttp

async def parallel_research(seed_keywords, max_concurrent=5):
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def research_single(session, seed):
        async with semaphore:
            url = "http://localhost:8000/api/research"
            data = {"seed_keyword": seed, "max_keywords": 25}
            
            async with session.post(url, json=data) as response:
                return await response.json()
    
    async with aiohttp.ClientSession() as session:
        tasks = [research_single(session, seed) for seed in seed_keywords]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return {seed: result for seed, result in zip(seed_keywords, results)}

# Usage
keywords = ["digital marketing", "content strategy", "seo", "ppc", "social media"]
results = asyncio.run(parallel_research(keywords))
```

## Troubleshooting Common Issues

### 1. Slow Response Times
- Reduce `max_keywords` parameter
- Use caching for repeated requests
- Check internet connection and API quotas
- Enable batch processing for multiple keywords

### 2. API Errors
- Verify OpenAI API key is valid and has credits
- Check rate limiting settings
- Monitor API usage in OpenAI dashboard
- Implement proper error handling and retries

### 3. Inconsistent Results
- Same seed keyword may generate different variations
- Use larger `max_keywords` for more consistent results
- AI responses have inherent variability
- Cache results for consistency within sessions

### 4. Memory Issues
- Reduce concurrent processing
- Clear results between large batch operations  
- Monitor system memory usage
- Use streaming for large datasets

## Best Practices

### 1. Keyword Research Strategy
- Start with broader seed keywords
- Use competitor analysis for inspiration
- Focus on long-tail opportunities for easier ranking
- Balance search volume with competition level

### 2. Result Analysis
- Prioritize keywords with 60+ opportunity score
- Consider search intent for content planning
- Look for question keywords for FAQ content
- Use CPC estimates for PPC budget planning

### 3. API Usage
- Implement proper error handling
- Use appropriate timeouts (30+ seconds)
- Cache frequently accessed results
- Monitor API quotas and usage

### 4. Integration
- Validate data before processing
- Handle API failures gracefully
- Log research sessions for analysis
- Set up monitoring and alerts

---

This usage guide covers the most common scenarios and advanced use cases. For specific integrations or custom requirements, refer to the API documentation or create custom scripts based on the examples provided.