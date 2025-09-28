# N8N Workflow Setup Guide

This guide explains how to configure and deploy the SEO Keyword Research AI Agent N8N workflow in different environments.

## Quick Setup

### 1. Import Workflow
1. Open your N8N instance
2. Click "Import from URL or JSON"
3. Paste the contents of `n8n-workflow.json`
4. Click "Import"

### 2. Configure Environment URLs

The workflow uses dynamic URLs that can be configured per execution. Set the `api_base_url` parameter in your workflow trigger:

#### For Development (Local)
```json
{
  "api_base_url": "http://localhost:8000",
  "seed_keyword": "digital marketing",
  "max_keywords": 50
}
```

#### For Production
```json
{
  "api_base_url": "https://your-production-api.com",
  "seed_keyword": "digital marketing",
  "max_keywords": 50
}
```

#### For Cloud Deployments

**Heroku:**
```json
{
  "api_base_url": "https://your-app-name.herokuapp.com",
  "seed_keyword": "digital marketing"
}
```

**Vercel:**
```json
{
  "api_base_url": "https://your-app-name.vercel.app",
  "seed_keyword": "digital marketing"
}
```

**Railway:**
```json
{
  "api_base_url": "https://your-app-name.railway.app",
  "seed_keyword": "digital marketing"
}
```

**DigitalOcean App Platform:**
```json
{
  "api_base_url": "https://your-app-name.ondigitalocean.app",
  "seed_keyword": "digital marketing"
}
```

## Deployment Options

### Option 1: Deploy API to Cloud Platform

Deploy the SEO Agent to a cloud platform and update the workflow:

#### Heroku Deployment
```bash
# Install Heroku CLI and login
heroku create your-seo-agent-app
git push heroku master
```

Then use URL: `https://your-seo-agent-app.herokuapp.com`

#### Vercel Deployment
```bash
# Install Vercel CLI
npm i -g vercel
vercel --prod
```

#### Railway Deployment
```bash
# Connect to Railway
railway login
railway deploy
```

### Option 2: Use N8N Environment Variables

Set global environment variables in N8N:

1. Go to N8N Settings → Environment Variables
2. Add: `SEO_API_BASE_URL=https://your-api-domain.com`
3. Update workflow to use: `{{ $env.SEO_API_BASE_URL }}`

### Option 3: Docker Deployment

Deploy both N8N and the SEO Agent using Docker Compose:

```yaml
# docker-compose.yml
version: '3.8'
services:
  seo-agent:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=password
    depends_on:
      - seo-agent
```

Then use URL: `http://seo-agent:8000` in the workflow.

## Workflow Configuration

### Required Credentials

#### Email (for reports)
- **Type**: SMTP
- **Host**: smtp.gmail.com (or your provider)
- **Port**: 587
- **User**: your-email@gmail.com
- **Password**: your-app-password

#### Slack (for notifications)
- **Webhook URL**: `https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK`
- **Channel**: `#seo-research`

#### Google Sheets (for logging)
- **Service Account**: Create in Google Cloud Console
- **Spreadsheet ID**: Get from Google Sheets URL
- **Sheet Name**: `SEO Keywords`

### Input Parameters

#### Single Keyword Research
```json
{
  "mode": "single",
  "api_base_url": "https://your-api-domain.com",
  "seed_keyword": "digital marketing",
  "max_keywords": 50,
  "country": "US",
  "include_questions": true,
  "include_long_tail": true
}
```

#### Batch Research
```json
{
  "mode": "batch",
  "api_base_url": "https://your-api-domain.com",
  "seed_keywords": [
    "digital marketing",
    "content strategy",
    "seo optimization"
  ],
  "max_keywords_each": 25,
  "country": "US"
}
```

## Trigger Options

### 1. Manual Trigger
- Use for on-demand keyword research
- Perfect for testing and ad-hoc requests

### 2. Schedule Trigger
```json
{
  "mode": "batch",
  "api_base_url": "https://your-api-domain.com",
  "seed_keywords": ["brand keywords", "competitor keywords"],
  "max_keywords_each": 25
}
```

Schedule: Every Monday at 9 AM

### 3. Webhook Trigger
Create a webhook endpoint to trigger research from external systems:

```bash
curl -X POST "https://your-n8n-instance.com/webhook/seo-research" \
  -H "Content-Type: application/json" \
  -d '{
    "api_base_url": "https://your-api-domain.com",
    "seed_keyword": "new product launch",
    "max_keywords": 50
  }'
```

### 4. Email Trigger
Monitor email for keyword research requests:
- Subject: "SEO Research Request"
- Body: Contains seed keywords

## Security Considerations

### 1. API Authentication
Add authentication to your SEO Agent API:

```python
# In web_server.py
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/api/research")
async def research_keywords(request: KeywordRequest, token: str = Depends(security)):
    # Validate token
    if not validate_token(token.credentials):
        raise HTTPException(status_code=401, detail="Invalid token")
    # ... rest of function
```

### 2. N8N Webhook Security
Add webhook authentication in N8N:
- Use HTTP Basic Auth
- Add custom headers for validation
- Whitelist IP addresses

### 3. Environment Variables
Never hardcode sensitive data:
```json
{
  "api_base_url": "{{ $env.SEO_API_URL }}",
  "api_key": "{{ $env.SEO_API_KEY }}"
}
```

## Testing the Workflow

### 1. Test Individual Nodes
- Run each node separately to verify configuration
- Check API connectivity
- Validate data transformations

### 2. End-to-End Testing
```json
{
  "mode": "single",
  "api_base_url": "https://your-test-api.com",
  "seed_keyword": "test keyword",
  "max_keywords": 5
}
```

### 3. Error Handling Testing
- Test with invalid API URLs
- Test with API timeouts
- Test with malformed responses

## Monitoring and Logging

### 1. N8N Execution Logs
- Monitor workflow execution history
- Set up alerts for failed executions
- Track performance metrics

### 2. API Monitoring
- Monitor API response times
- Track API usage and costs
- Set up health checks

### 3. Notification Setup
Configure alerts for:
- Workflow failures
- API errors
- High usage warnings

## Troubleshooting

### Common Issues

#### 1. Connection Timeout
```
Error: connect ECONNREFUSED
```
**Solution**: Verify API URL and ensure service is running

#### 2. Authentication Errors
```
Error: 401 Unauthorized
```
**Solution**: Check API keys and authentication setup

#### 3. Rate Limiting
```
Error: 429 Too Many Requests
```
**Solution**: Add delays between requests or reduce batch sizes

### Debug Mode
Enable debug logging in N8N:
```bash
N8N_LOG_LEVEL=debug
```

## Production Checklist

- [ ] API deployed to production environment
- [ ] N8N workflow imported and tested
- [ ] All credentials configured securely
- [ ] Email notifications working
- [ ] Slack notifications working
- [ ] Google Sheets logging working
- [ ] Error handling tested
- [ ] Performance monitoring setup
- [ ] Security measures implemented
- [ ] Backup and recovery plan in place

## Support

For workflow-specific issues:
1. Check N8N execution logs
2. Verify API endpoint accessibility
3. Test individual workflow nodes
4. Check environment variable configuration

For API issues, refer to the main project documentation.

---

**Note**: Always test the workflow in a development environment before deploying to production. The workflow can generate significant API costs if not properly configured with rate limiting and error handling.