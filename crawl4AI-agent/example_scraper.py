import asyncio
from datetime import datetime
from crawl4ai import AsyncWebCrawler
from pydantic_ai_expert import pydantic_ai_expert

async def main():
    # Get the URL from command line or use a default
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    print(f"Crawling URL: {url}")
    # Initialize the crawler
    async with AsyncWebCrawler() as crawler:
        # Crawl the page
        result = await crawler.arun(
            url=url,
            # Optional parameters:
            # max_depth=2,  # How many links deep to crawl
            # max_pages=10,  # Maximum number of pages to crawl
            # allowed_domains=["example.com"],  # Restrict crawling to these domains
        )
        
        # Print the scraped content in markdown format
        print("\nScraped Content:")
        print("-" * 50)
        print(f"Title: {result.title}")
        print(f"Number of links found: {len(result.links)}")
        print("-" * 50)
        print(result.markdown)
        print("-" * 50)
        
        print("\nStoring in Supabase...")
        expert = pydantic_ai_expert()
        await expert.store_page(
            url=url,
            title=result.title,
            content=result.text,
            metadata={
                "source": "web_crawler",
                "timestamp": str(datetime.now()),
                "num_links": len(result.links)
            }
        )
        print("Content stored successfully!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {str(e)}")
