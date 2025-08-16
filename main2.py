import asyncio
import httpx
import time
token = "sk_OIWw3O1JOZSg91rvK41nLLPXKxePYO09FTcSJt4GSPLn1y0ic0L4c9TBywdstds1"
url="https://viidedss.com/dc/?blockID=382755"
payload = {
    "actor": "unlocker.webunlocker",
    "proxy": {
        "country": "US"
    },
    "input": {
        "url": url,
        "jsRender": {
            "enabled": True,
            "waitUntil":"domcontentloaded",
            "instructions":[{"wait": 8000}],
            "response": {
                "type": "html",  # png or jpeg
            }
        },
    }
}


async def fetch_url(client, url):
    """
    Asynchronously fetches a single URL and returns its JSON content.
    """
    try:
        # The 'await' keyword pauses this task until the response is received.
        response = await client.post( "https://api.scrapeless.com/api/v2/unlocker/request",
	    json=payload,
	    headers={
	        "x-api-token": token,
	        "Content-Type": "application/json"
	    },
	    timeout=60)
        # Raise an exception for bad status codes (4xx or 5xx).
        
        return response.json()
    except httpx.HTTPError as exc:
        return f"An HTTP error occurred for {exc.request.url!r}."
    except Exception as exc:
        return f"An unexpected error occurred for {url}: {exc}"

async def main():
    url="https://api.scrapeless.com/api/v2/unlocker/request"
    """
    Main asynchronous function to run all requests concurrently.
    """
    print("Starting 5 concurrent requests with httpx...")
    start_time = time.time()

    # Create a single AsyncClient session to share across all requests.
    async with httpx.AsyncClient() as client:
        # Create a list of 'tasks' to be run concurrently.
        # Each task is an awaitable object returned by fetch_url.
        tasks = [fetch_url(client, url) for _ in range(5)]

        # Use asyncio.gather() to run all tasks at once.
        # The results will be returned in the order the tasks were created.
        results = await asyncio.gather(*tasks)

    end_time = time.time()
    print("All requests completed.")
    print(f"Total time taken: {end_time - start_time:.2f} seconds.")
    
  
if __name__ == "__main__":
    for i in range(1000):
      asyncio.run(main())
      print(i)
