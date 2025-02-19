import asyncio
from crawl4ai import AsyncWebCrawler
from pydantic_ai_expert import pydantic_ai_expert

async def main():
    # Initialize the crawler
    async with AsyncWebCrawler() as crawler:
        # Replace this URL with the website you want to scrape
        url = "https://example.com"
        
        # Crawl the page
        result = await crawler.arun(
            url=url,
            # Optional parameters:
            # max_depth=2,  # How many links deep to crawl
            # max_pages=10,  # Maximum number of pages to crawl
            # allowed_domains=["example.com"],  # Restrict crawling to these domains
        )
        
        # Print the scraped content in markdown format
        print("Scraped Content:")
        print(result.markdown)
        
        # The result also contains:
        # result.text - plain text content
        # result.html - raw HTML content
        # result.links - list of links found on the page
        # result.title - page title
        
        # You can also store the results in Supabase using the pydantic_ai_expert
        expert = pydantic_ai_expert()
        await expert.store_page(
            url=url,
            title=result.title,
            content=result.text,
            metadata={
                "source": "web_crawler",
                "timestamp": str(datetime.now())
            }
        )

if __name__ == "__main__":
    asyncio.run(main())
