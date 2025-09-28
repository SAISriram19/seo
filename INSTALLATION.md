# Installation Guide

This guide provides detailed installation instructions for the SEO Keyword Research AI Agent on different operating systems.

## System Requirements

### Minimum Requirements
- Python 3.8 or higher
- 4 GB RAM
- 1 GB free disk space
- Internet connection for API calls

### Recommended Requirements
- Python 3.9+
- 8 GB RAM
- 2 GB free disk space
- Stable internet connection (100+ Mbps)

## Prerequisites

### 1. Python Installation

#### Windows
1. Download Python from [python.org](https://python.org)
2. Run the installer and check "Add Python to PATH"
3. Verify installation:
   ```cmd
   python --version
   pip --version
   ```

#### macOS
1. Install using Homebrew:
   ```bash
   brew install python@3.9
   ```
2. Or download from [python.org](https://python.org)

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.9 python3.9-pip python3.9-venv
```

### 2. Git Installation
- **Windows**: Download from [git-scm.com](https://git-scm.com)
- **macOS**: `brew install git`
- **Linux**: `sudo apt install git`

### 3. API Keys Setup

#### OpenAI API Key (Required)
1. Visit [OpenAI Platform](https://platform.openai.com)
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and save the key securely

#### SerpAPI Key (Optional)
1. Visit [SerpAPI](https://serpapi.com)
2. Sign up for a free account
3. Get your API key from dashboard
4. Note: Free tier includes 100 searches/month

## Installation Methods

### Method 1: Quick Installation (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/SAISriram19/seo.git
   cd seo
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv seo-env
   seo-env\Scripts\activate

   # macOS/Linux
   python3 -m venv seo-env
   source seo-env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   # Create .env file
   cp .env.example .env  # If example exists
   # Or create manually
   ```

   Edit `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPAPI_KEY=your_serpapi_key_here
   ```

5. **Test installation**
   ```bash
   python -c "import seo_agent_pro; print('Installation successful!')"
   ```

### Method 2: Docker Installation

1. **Prerequisites**
   - Docker installed and running
   - Docker Compose (optional)

2. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8000

   CMD ["python", "web_server.py"]
   ```

3. **Build and run**
   ```bash
   docker build -t seo-agent .
   docker run -p 8000:8000 --env-file .env seo-agent
   ```

### Method 3: Development Installation

For contributors and developers:

1. **Clone with development branch**
   ```bash
   git clone https://github.com/SAISriram19/seo.git
   cd seo
   git checkout develop  # If development branch exists
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If exists
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install  # If using pre-commit
   ```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
OPENAI_API_KEY=sk-your-openai-key-here

# Optional
SERPAPI_KEY=your-serpapi-key-here

# Application Settings
HOST=0.0.0.0
PORT=8000
DEBUG=false

# Logging
LOG_LEVEL=INFO
LOG_FILE=seo_agent.log

# Performance
MAX_WORKERS=10
REQUEST_TIMEOUT=30
```

### Advanced Configuration

#### Custom API Endpoints
```env
# Custom OpenAI endpoint (for Azure OpenAI)
OPENAI_BASE_URL=https://your-resource.openai.azure.com
OPENAI_API_VERSION=2023-05-15

# Custom model settings
DEFAULT_MODEL=gpt-4o-mini
FALLBACK_MODEL=gpt-3.5-turbo
MAX_TOKENS=2000
TEMPERATURE=0.7
```

#### Performance Tuning
```env
# Batch processing
BATCH_SIZE=20
BATCH_DELAY=0.5

# Caching
ENABLE_CACHE=true
CACHE_TTL=3600

# Rate limiting
REQUESTS_PER_MINUTE=60
BURST_LIMIT=10
```

## Verification

### 1. Basic Functionality Test
```bash
python seo_agent_pro.py
```

Expected output:
```
PRODUCTION SEO Keyword Research AI Agent
========================================
[+] Real OpenAI GPT-4 integration
[+] Professional SEO metrics
[+] CSV/JSON export
[+] Batch processing
```

### 2. Web Interface Test
```bash
python web_server.py
```

Open browser to `http://localhost:8000`

### 3. API Test
```bash
curl -X POST "http://localhost:8000/api/health"
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00",
  "agent_initialized": true
}
```

### 4. Full Integration Test
```bash
curl -X POST "http://localhost:8000/api/research" \
  -H "Content-Type: application/json" \
  -d '{"seed_keyword": "test", "max_keywords": 5}'
```

## Troubleshooting

### Common Issues

#### 1. Import Errors
**Error**: `ModuleNotFoundError: No module named 'openai'`

**Solution**:
```bash
pip install --upgrade openai
```

#### 2. API Key Errors
**Error**: `OpenAI API key is required in .env file`

**Solutions**:
- Verify `.env` file exists in project root
- Check API key format (starts with `sk-`)
- Ensure no extra spaces in `.env` file
- Restart application after updating `.env`

#### 3. Permission Errors
**Error**: `PermissionError: [Errno 13] Permission denied`

**Solutions**:
```bash
# Windows
# Run as administrator or check file permissions

# macOS/Linux
chmod +x web_server.py
sudo chown -R $USER:$USER /path/to/project
```

#### 4. Port Already in Use
**Error**: `OSError: [Errno 48] Address already in use`

**Solutions**:
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process or use different port
export PORT=8001
python web_server.py
```

#### 5. Network/Firewall Issues
**Symptoms**: API calls timing out

**Solutions**:
- Check internet connection
- Verify firewall settings
- Test API connectivity:
  ```bash
  curl https://api.openai.com/v1/models \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

### Performance Issues

#### Slow Response Times
1. Check API key usage limits
2. Reduce `max_keywords` parameter
3. Enable caching in `.env`:
   ```env
   ENABLE_CACHE=true
   ```

#### Memory Issues
1. Reduce `MAX_WORKERS` in `.env`
2. Process keywords in smaller batches
3. Monitor memory usage:
   ```bash
   # Linux/macOS
   top -p $(pgrep -f web_server.py)
   
   # Windows
   tasklist | findstr python
   ```

### Debugging Mode

Enable debug mode for detailed logging:

```env
DEBUG=true
LOG_LEVEL=DEBUG
```

Or run with verbose output:
```bash
python web_server.py --debug
```

## Uninstallation

### Complete Removal
```bash
# Deactivate virtual environment
deactivate

# Remove project directory
rm -rf /path/to/seo-keyword-agent

# Remove virtual environment
rm -rf seo-env

# Clean pip cache
pip cache purge
```

### Keep Configuration
```bash
# Backup configuration
cp .env ~/.seo-agent-backup.env

# Remove application but keep config
rm -rf seo-keyword-agent
mkdir seo-keyword-agent
cp ~/.seo-agent-backup.env seo-keyword-agent/.env
```

## Next Steps

After successful installation:

1. Read `USAGE.md` for detailed usage instructions
2. Check `API_DOCUMENTATION.md` for API reference
3. Explore the web interface at `http://localhost:8000`
4. Try the N8N workflow templates for automation

## Support

For installation issues:

1. Check the troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with:
   - Operating system and version
   - Python version
   - Error messages
   - Installation method used

## Version Notes

### v1.0.0
- Initial release
- Python 3.8+ support
- Cross-platform compatibility
- Docker support

---

**Note**: Keep your API keys secure and never commit them to version control. Use environment variables or secure key management systems in production.