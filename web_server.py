"""
FastAPI Web Server for SEO Keyword Research AI Agent
- Modern web interface
- Real-time API endpoints
- Export functionality
- Production ready
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import json
import io
import csv
from datetime import datetime

from seo_agent_pro import ProductionSEOAgent

# Pydantic models
class KeywordRequest(BaseModel):
    seed_keyword: str
    max_keywords: int = 50
    country: str = "US"
    include_questions: bool = True
    include_long_tail: bool = True

class BatchRequest(BaseModel):
    seed_keywords: List[str]
    max_keywords_each: int = 25
    country: str = "US"

# Initialize FastAPI app
app = FastAPI(
    title="SEO Keyword Research AI Agent",
    description="Production-grade AI-powered keyword research tool",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize SEO agent
seo_agent = None

@app.on_event("startup")
async def startup_event():
    global seo_agent
    seo_agent = ProductionSEOAgent()

@app.on_event("shutdown")
async def shutdown_event():
    if seo_agent:
        await seo_agent.close()

# API Endpoints
@app.post("/api/research")
async def research_keywords(request: KeywordRequest):
    """Research keywords endpoint"""
    
    if not seo_agent:
        raise HTTPException(status_code=500, detail="SEO agent not initialized")
    
    try:
        result = await seo_agent.research_keywords(
            seed_keyword=request.seed_keyword,
            max_keywords=request.max_keywords,
            country=request.country,
            include_questions=request.include_questions,
            include_long_tail=request.include_long_tail
        )
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/batch-research")
async def batch_research(request: BatchRequest):
    """Batch research keywords endpoint"""
    
    if not seo_agent:
        raise HTTPException(status_code=500, detail="SEO agent not initialized")
    
    try:
        results = await seo_agent.batch_research(
            seed_keywords=request.seed_keywords,
            max_keywords_each=request.max_keywords_each,
            country=request.country
        )
        return results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/export/csv")
async def export_csv(request: KeywordRequest):
    """Export keywords to CSV"""
    
    if not seo_agent:
        raise HTTPException(status_code=500, detail="SEO agent not initialized")
    
    try:
        # Get research results
        result = await seo_agent.research_keywords(
            seed_keyword=request.seed_keyword,
            max_keywords=request.max_keywords,
            country=request.country,
            include_questions=request.include_questions,
            include_long_tail=request.include_long_tail
        )
        
        # Generate CSV
        csv_data = seo_agent.export_to_csv(result)
        
        # Return as streaming response
        output = io.StringIO(csv_data)
        
        return StreamingResponse(
            io.BytesIO(csv_data.encode('utf-8')),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=keywords_{request.seed_keyword.replace(' ', '_')}.csv"}
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "agent_initialized": seo_agent is not None
    }

# Web Interface
@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main web interface"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEO Keyword Research AI Agent</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body { 
            font-family: 'Inter', sans-serif;
            background-color: #000000;
            color: #ffffff;
        }
        
        .dark-bg {
            background-color: #000000;
        }
        
        .keyword-card {
            transition: all 0.3s ease;
            border-left: 4px solid #ffffff;
            background-color: #111111;
            border: 1px solid #333333;
        }
        
        .keyword-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255,255,255,0.1);
            background-color: #1a1a1a;
        }
        
        .loading {
            border: 3px solid #333333;
            border-top: 3px solid #ffffff;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .badge {
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
        }
        
        .badge-high { background-color: #333333; color: #ffffff; border: 1px solid #666666; }
        .badge-medium { background-color: #666666; color: #ffffff; }
        .badge-low { background-color: #999999; color: #000000; }
        
        input, select {
            background-color: #111111;
            border-color: #333333;
            color: #ffffff;
        }
        
        input:focus, select:focus {
            border-color: #ffffff;
            box-shadow: 0 0 0 2px rgba(255,255,255,0.2);
        }
        
        .btn-primary {
            background-color: #ffffff;
            color: #000000;
        }
        
        .btn-primary:hover {
            background-color: #cccccc;
        }
        
        .btn-secondary {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #666666;
        }
        
        .btn-secondary:hover {
            background-color: #555555;
        }
    </style>
</head>
<body class="bg-black text-white">
    <!-- Header -->
    <header class="dark-bg border-b border-gray-800">
        <div class="container mx-auto px-6 py-8">
            <h1 class="text-4xl font-bold mb-2 text-white">SEO Keyword Research AI Agent</h1>
            <p class="text-xl text-gray-300">Production-grade AI-powered keyword research platform</p>
        </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto px-6 py-8">
        <!-- Research Form -->
        <div class="bg-gray-900 rounded-lg border border-gray-700 p-8 mb-8">
            <h2 class="text-2xl font-semibold mb-6 text-white">Keyword Research</h2>
            
            <form id="keywordForm" class="space-y-6">
                <div class="grid md:grid-cols-2 gap-6">
                    <div>
                        <label for="seedKeyword" class="block text-sm font-medium text-gray-300 mb-2">Seed Keyword *</label>
                        <input type="text" id="seedKeyword" name="seedKeyword" required
                               class="w-full px-4 py-3 bg-gray-800 border border-gray-600 rounded-lg text-white focus:border-white"
                               placeholder="e.g., digital marketing">
                    </div>
                    
                    <div>
                        <label for="maxKeywords" class="block text-sm font-medium text-gray-300 mb-2">Max Keywords</label>
                        <select id="maxKeywords" name="maxKeywords" 
                                class="w-full px-4 py-3 bg-gray-800 border border-gray-600 rounded-lg text-white focus:border-white">
                            <option value="25">25 keywords</option>
                            <option value="50" selected>50 keywords</option>
                            <option value="75">75 keywords</option>
                            <option value="100">100 keywords</option>
                        </select>
                    </div>
                </div>
                
                <div class="grid md:grid-cols-3 gap-4">
                    <div>
                        <label for="country" class="block text-sm font-medium text-gray-300 mb-2">Target Country</label>
                        <select id="country" name="country" 
                                class="w-full px-4 py-3 bg-gray-800 border border-gray-600 rounded-lg text-white focus:border-white">
                            <option value="US" selected>United States</option>
                            <option value="GB">United Kingdom</option>
                            <option value="CA">Canada</option>
                            <option value="AU">Australia</option>
                            <option value="IN">India</option>
                        </select>
                    </div>
                    
                    <div class="flex items-center">
                        <input type="checkbox" id="includeQuestions" name="includeQuestions" checked 
                               class="rounded border-gray-600 bg-gray-800 text-white">
                        <label for="includeQuestions" class="ml-2 text-sm font-medium text-gray-300">Include Questions</label>
                    </div>
                    
                    <div class="flex items-center">
                        <input type="checkbox" id="includeLongTail" name="includeLongTail" checked 
                               class="rounded border-gray-600 bg-gray-800 text-white">
                        <label for="includeLongTail" class="ml-2 text-sm font-medium text-gray-300">Include Long-tail</label>
                    </div>
                </div>
                
                <div class="flex gap-4">
                    <button type="submit" id="researchBtn" 
                            class="btn-primary font-semibold py-3 px-8 rounded-lg transition duration-300">
                        Research Keywords
                    </button>
                    
                    <button type="button" id="exportCsvBtn" 
                            class="btn-secondary font-semibold py-3 px-8 rounded-lg transition duration-300"
                            disabled>
                        Export CSV
                    </button>
                </div>
            </form>
        </div>

        <!-- Loading State -->
        <div id="loadingState" class="hidden bg-gray-900 rounded-lg border border-gray-700 p-8 mb-8">
            <div class="flex items-center justify-center space-x-4">
                <div class="loading"></div>
                <div>
                    <p class="text-lg font-semibold text-white">AI is researching keywords...</p>
                    <p class="text-gray-300">Using real OpenAI GPT-4 and advanced SEO metrics</p>
                </div>
            </div>
        </div>

        <!-- Results Section -->
        <div id="resultsSection" class="hidden">
            <!-- Summary Stats -->
            <div id="summaryStats" class="grid md:grid-cols-4 gap-4 mb-8">
                <!-- Stats will be populated here -->
            </div>

            <!-- Keywords List -->
            <div class="bg-gray-900 rounded-lg border border-gray-700">
                <div class="px-6 py-4 bg-gray-800 border-b border-gray-700">
                    <h3 class="text-lg font-semibold text-white">Keyword Opportunities</h3>
                </div>
                
                <div id="keywordsList" class="p-6">
                    <!-- Keywords will be populated here -->
                </div>
            </div>
        </div>

        <!-- Error State -->
        <div id="errorState" class="hidden bg-gray-900 border border-gray-600 rounded-lg p-6 mb-8">
            <div class="flex items-center space-x-3">
                <div class="text-gray-400 text-xl">!</div>
                <div>
                    <h3 class="text-lg font-semibold text-white">Error</h3>
                    <p id="errorMessage" class="text-gray-300"></p>
                </div>
            </div>
        </div>
    </main>

    <script>
        let currentResults = null;

        document.getElementById('keywordForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(e.target);
            const requestData = {
                seed_keyword: formData.get('seedKeyword'),
                max_keywords: parseInt(formData.get('maxKeywords')),
                country: formData.get('country'),
                include_questions: formData.has('includeQuestions'),
                include_long_tail: formData.has('includeLongTail')
            };

            await researchKeywords(requestData);
        });

        document.getElementById('exportCsvBtn').addEventListener('click', async () => {
            if (currentResults) {
                await exportToCsv(currentResults);
            }
        });

        async function researchKeywords(requestData) {
            try {
                showLoading();
                hideError();
                
                const response = await fetch('/api/research', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(requestData)
                });

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${await response.text()}`);
                }

                const data = await response.json();
                currentResults = data;
                displayResults(data);
                
            } catch (error) {
                console.error('Error:', error);
                showError(error.message);
            } finally {
                hideLoading();
            }
        }

        async function exportToCsv(results) {
            try {
                const requestData = {
                    seed_keyword: results.seed_keyword,
                    max_keywords: results.total_keywords,
                    country: results.country || "US",
                    include_questions: true,
                    include_long_tail: true
                };

                const response = await fetch('/api/export/csv', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(requestData)
                });

                if (response.ok) {
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `keywords_${results.seed_keyword.replace(' ', '_')}.csv`;
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    document.body.removeChild(a);
                } else {
                    throw new Error('Export failed');
                }
            } catch (error) {
                alert('Export failed: ' + error.message);
            }
        }

        function showLoading() {
            document.getElementById('loadingState').classList.remove('hidden');
            document.getElementById('resultsSection').classList.add('hidden');
            document.getElementById('researchBtn').disabled = true;
            document.getElementById('exportCsvBtn').disabled = true;
        }

        function hideLoading() {
            document.getElementById('loadingState').classList.add('hidden');
            document.getElementById('researchBtn').disabled = false;
        }

        function showError(message) {
            document.getElementById('errorMessage').textContent = message;
            document.getElementById('errorState').classList.remove('hidden');
            document.getElementById('resultsSection').classList.add('hidden');
        }

        function hideError() {
            document.getElementById('errorState').classList.add('hidden');
        }

        function displayResults(data) {
            displaySummaryStats(data);
            displayKeywords(data.keywords);
            document.getElementById('resultsSection').classList.remove('hidden');
            document.getElementById('exportCsvBtn').disabled = false;
        }

        function displaySummaryStats(data) {
            const stats = [
                {
                    title: 'Total Keywords',
                    value: data.total_keywords
                },
                {
                    title: 'Processing Time',
                    value: `${data.processing_time}s`
                },
                {
                    title: 'API Calls',
                    value: data.metadata?.api_calls || 0
                },
                {
                    title: 'Avg Opportunity',
                    value: Math.round(data.keywords.reduce((sum, k) => sum + k.opportunity_score, 0) / data.keywords.length)
                }
            ];

            const statsHTML = stats.map(stat => `
                <div class="bg-gray-900 rounded-lg border border-gray-700 p-6 text-center">
                    <div class="text-2xl font-bold text-white">${stat.value}</div>
                    <div class="text-sm text-gray-300">${stat.title}</div>
                </div>
            `).join('');

            document.getElementById('summaryStats').innerHTML = statsHTML;
        }

        function displayKeywords(keywords) {
            const keywordsHTML = keywords.map((keyword, index) => {
                const difficultyClass = keyword.difficulty <= 30 ? 'badge-low' : 
                                      keyword.difficulty <= 60 ? 'badge-medium' : 'badge-high';
                const difficultyText = keyword.difficulty <= 30 ? 'Easy' : 
                                     keyword.difficulty <= 60 ? 'Medium' : 'Hard';
                
                return `
                    <div class="keyword-card p-4 mb-4">
                        <div class="flex items-center justify-between mb-3">
                            <h4 class="text-lg font-semibold text-white">${keyword.keyword}</h4>
                            <div class="flex items-center space-x-2">
                                <span class="text-2xl font-bold text-white">${keyword.opportunity_score}</span>
                                <span class="text-sm text-gray-400">score</span>
                            </div>
                        </div>
                        
                        <div class="grid md:grid-cols-4 gap-4 text-sm">
                            <div>
                                <span class="text-gray-400">Search Volume</span>
                                <div class="font-semibold text-gray-200">${keyword.search_volume.toLocaleString()}</div>
                            </div>
                            <div>
                                <span class="text-gray-400">Difficulty</span>
                                <div class="flex items-center space-x-2">
                                    <span class="badge ${difficultyClass}">${difficultyText}</span>
                                    <span class="text-gray-400">${keyword.difficulty}/100</span>
                                </div>
                            </div>
                            <div>
                                <span class="text-gray-400">Intent</span>
                                <div class="font-semibold text-gray-200 capitalize">${keyword.intent}</div>
                            </div>
                            <div>
                                <span class="text-gray-400">CPC Estimate</span>
                                <div class="font-semibold text-gray-200">$${keyword.cpc_estimate}</div>
                            </div>
                        </div>
                        
                        <div class="mt-3 pt-3 border-t border-gray-700">
                            <div class="flex items-center justify-between text-sm">
                                <span class="text-gray-400">Ranking Probability: <strong class="text-gray-200">${Math.round(keyword.ranking_probability * 100)}%</strong></span>
                                <span class="text-gray-400">Competition: <strong class="text-gray-200">${keyword.competition_score}</strong></span>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');

            document.getElementById('keywordsList').innerHTML = keywordsHTML;
        }
    </script>
</body>
</html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)