import asyncio
from seo_agent import SEOKeywordAgent

async def test_global_internship():
    agent = SEOKeywordAgent()
    result = await agent.research_keywords('global internship', max_keywords=15)
    
    print('\n🎯 TOP RESULTS FOR "GLOBAL INTERNSHIP":')
    print('=' * 90)
    for i, kw in enumerate(result['keywords'], 1):
        print(f'{i:2d}. {kw["keyword"]:<40} Score: {kw["opportunity_score"]:5.1f} | '
              f'Volume: {kw["search_volume"]:>6,} | Intent: {kw["intent"]}')
    
    print(f'\n⚡ Generated {result["total_keywords"]} keywords in {result["processing_time"]}s')
    print('\n💰 This used REAL OpenAI API calls with your API key!')

if __name__ == "__main__":
    asyncio.run(test_global_internship())