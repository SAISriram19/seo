# SEO Keyword Research AI Agent

A production-grade AI-powered keyword research tool that leverages OpenAI GPT-4 to generate and analyze SEO keyword opportunities with real-time metrics and competitive analysis.

## Features

- **AI-Powered Keyword Generation**: Uses OpenAI GPT-4 to generate semantic keyword variations
- **Real-time SEO Metrics**: Analyzes search volume, competition, and difficulty scores
- **Intelligent Ranking**: Advanced opportunity scoring algorithm for first-page ranking potential
- **Modern Web Interface**: Clean, responsive web UI with real-time results
- **Multiple Export Formats**: CSV and JSON export capabilities
- **Batch Processing**: Research multiple seed keywords simultaneously
- **API Integration**: RESTful API for programmatic access
- **N8N Workflow Support**: Pre-built automation workflows

## Technology Stack

- **Backend**: Python 3.8+, FastAPI
- **AI Integration**: OpenAI GPT-4 API
- **SEO APIs**: SerpAPI integration (optional)
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Database**: In-memory processing with optional caching
- **Automation**: N8N workflow templates

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- SerpAPI key (optional, for enhanced search volume data)

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SAISriram19/seo.git
   cd seo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPAPI_KEY=your_serpapi_key_here  # Optional
   ```

4. **Run the application**
   ```bash
   python web_server.py
   ```

5. **Access the web interface**
   
   Open your browser and navigate to: `http://localhost:8000`

## Usage

### Web Interface

1. **Single Keyword Research**
   - Enter your seed keyword (e.g., "digital marketing")
   - Select maximum number of keywords (25-100)
   - Choose target country
   - Toggle question-based and long-tail keyword options
   - Click "Research Keywords" to generate results

2. **Batch Processing**
   - Use the API endpoint `/api/batch-research`
   - Submit multiple seed keywords for simultaneous processing

3. **Export Results**
   - Export results in CSV or JSON format
   - Download directly from the web interface

### Command Line Interface

```bash
python seo_agent_pro.py
```

Follow the interactive prompts for:
- Single keyword research
- Batch keyword research
- Export options

### API Usage

#### Single Keyword Research
```bash
curl -X POST "http://localhost:8000/api/research" \
  -H "Content-Type: application/json" \
  -d '{
    "seed_keyword": "digital marketing",
    "max_keywords": 50,
    "country": "US",
    "include_questions": true,
    "include_long_tail": true
  }'
```

#### Batch Research
```bash
curl -X POST "http://localhost:8000/api/batch-research" \
  -H "Content-Type: application/json" \
  -d '{
    "seed_keywords": ["digital marketing", "content strategy"],
    "max_keywords_each": 25,
    "country": "US"
  }'
```

#### Export to CSV
```bash
curl -X POST "http://localhost:8000/api/export/csv" \
  -H "Content-Type: application/json" \
  -d '{
    "seed_keyword": "digital marketing",
    "max_keywords": 50,
    "country": "US"
  }' \
  --output keywords.csv
```

## Keyword Metrics

Each generated keyword includes comprehensive SEO metrics:

- **Opportunity Score** (0-100): Weighted score considering volume, competition, and difficulty
- **Search Volume**: Estimated monthly search volume
- **Competition Score** (0-1): Competition level analysis
- **Keyword Difficulty** (1-100): Ranking difficulty assessment
- **Search Intent**: Classified as informational, commercial, transactional, or navigational
- **CPC Estimate**: Estimated cost per click for paid advertising
- **Ranking Probability**: Likelihood of achieving first-page rankings

## Algorithm Details

### Opportunity Score Calculation

The opportunity score uses a weighted algorithm:

```
Score = (Volume × 0.35) + (Competition × 0.35) + (Difficulty × 0.20) + (Intent × 0.10)
```

Where:
- **Volume**: Normalized search volume (0-100)
- **Competition**: Inverse competition score (lower = better)
- **Difficulty**: Inverse difficulty score (lower = better)
- **Intent**: Weighted by commercial value (transactional > commercial > informational)

### Keyword Generation Process

1. **AI-Powered Expansion**: GPT-4 generates semantic variations
2. **Pattern-Based Enhancement**: Applies proven SEO keyword patterns
3. **Intent Classification**: AI-powered search intent analysis
4. **Metrics Collection**: Real-time SEO data gathering
5. **Intelligent Ranking**: Multi-factor opportunity scoring

## Project Structure

```
seo-keyword-agent/
├── seo_agent_pro.py          # Main AI agent implementation
├── web_server.py             # FastAPI web server
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── test_demo.py             # Test suite
├── n8n-workflow.json        # N8N automation workflow
├── N8N_WORKFLOW_SETUP.md    # N8N deployment guide
├── README.md                # This file
├── INSTALLATION.md          # Detailed installation guide
├── API_DOCUMENTATION.md     # Complete API reference
└── USAGE.md                 # Usage examples and tutorials
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 access | Yes |
| `SERPAPI_KEY` | SerpAPI key for enhanced search data | No |

### Customization Options

- **Keyword Generation**: Modify prompts in `_generate_keywords_ai()`
- **Scoring Algorithm**: Adjust weights in `_calculate_opportunity_score()`
- **Competition Analysis**: Update factors in `_calculate_competition()`
- **Intent Classification**: Enhance patterns in `_classify_intent_smart()`

## API Reference

### Endpoints

- `POST /api/research` - Single keyword research
- `POST /api/batch-research` - Batch keyword research
- `POST /api/export/csv` - Export results to CSV
- `GET /api/health` - Health check endpoint

### Request/Response Examples

See `API_DOCUMENTATION.md` for complete API reference with examples.

## Error Handling

The system includes comprehensive error handling:

- **API Rate Limits**: Automatic retry with exponential backoff
- **Invalid Keywords**: Input validation and sanitization
- **Network Errors**: Graceful fallback to backup methods
- **AI Service Unavailable**: Smart fallback keyword generation

## Performance Optimization

- **Parallel Processing**: Concurrent API calls for faster results
- **Intelligent Caching**: Reduces redundant API calls
- **Batch Operations**: Efficient processing of multiple keywords
- **Memory Management**: Optimized for large keyword sets

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## N8N Workflow Deployment

The included N8N workflow provides enterprise automation capabilities:

### Quick Setup
1. **Import Workflow**: Use `n8n-workflow.json` in your N8N instance
2. **Configure URLs**: Set your API endpoint (not localhost for production)
3. **Add Credentials**: Configure email, Slack, and Google Sheets
4. **Test**: Run a sample workflow

### Production Deployment
For production use, deploy the API to a cloud platform:

- **Heroku**: `https://your-app.herokuapp.com`
- **Vercel**: `https://your-app.vercel.app`
- **Railway**: `https://your-app.railway.app`
- **DigitalOcean**: `https://your-app.ondigitalocean.app`

See `N8N_WORKFLOW_SETUP.md` for complete deployment guide with security considerations, authentication setup, and troubleshooting.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or contributions:

1. **Issues**: Submit via GitHub Issues
2. **Documentation**: Check the `/docs` folder for detailed guides
3. **API Help**: See `API_DOCUMENTATION.md`
4. **Installation**: See `INSTALLATION.md`

## Changelog

### Version 1.0.0 (Current)
- Initial production release
- OpenAI GPT-4 integration
- Web interface with modern UI
- RESTful API endpoints
- CSV/JSON export functionality
- N8N workflow templates
- Comprehensive documentation

---

**Note**: This is a production-grade tool designed for professional SEO keyword research. Ensure you have valid API keys and understand any associated costs before running extensive keyword research campaigns.