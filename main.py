"""print("start1")
import asyncio
import aiohttp  # Requires installing: pip install aiohttp
from random import randint

async def fetch_url(session, url):
    """Asynchronously fetches the content of a URL using aiohttp."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return await response.text()  # Or response.read() for binary data
    except aiohttp.ClientError as e:  # Catch connection errors and HTTP errors
        print(f"Error fetching {url}: {e}")
        return None


async def main():
    """Creates an aiohttp session and fetches multiple URLs concurrently."""
    urls = list()
    apis =[
        "ZcGJICpMgs97mq6RPfubaim3Zy7pEFdf","bE0pN0b3maxrsVQkzp7igYfHY9KceJIE"]
    #ad ="https://www.effectiveratecpm.com/ca83bzpx98?key=dee9c6f3171b614287718132222041ad"
    #ad = "https://www.profitableratecpm.com/zhzbtigdvk?key=bfdf77a1bedb6a88e866ad888aa3896b"
    ad ="https://www.profitableratecpm.com/mrrsnt73cz?key=a9264f3ab1770607dd37951c2da5963c"
    #ad ="https://www.profitableratecpm.com/bygzdn8ti5?key=ac2134fc257fcbc83800d460291ac1ab"
    ad ="https://viinnqwx.com/dc/?blockID=382412"
    #ad="https://www.profitableratecpm.com/es8iaffr0n?key=a180891d7e00848a91909a7b8081d758"
    ad="https://www.profitableratecpm.com/ziz6kzsc0s?key=ca1c1f39a7636892a713e4f321013c96"
    for api in apis:
        for _ in range(randint (3,5)):
            url = f"https://api.webscrapingapi.com/v2?api_key={api}&url={ad}&country=ca&render_js=1"
            urls.append(url)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)  # Run all tasks concurrently

    # Process the results (optional)
    for i, result in enumerate(results):
        if result:
            print("proxy" in result)
        else:
            print(f"Failed to fetch {urls[i]}")


if __name__ == "__main__":
   for i in range (1000):
     print(i)
     asyncio.run(main())"""

import asyncio
import httpx
import time
token = "sk_OIWw3O1JOZSg91rvK41nLLPXKxePYO09FTcSJt4GSPLn1y0ic0L4c9TBywdstds1"
url="https://www.profitableratecpm.com/ziz6kzsc0s?key=ca1c1f39a7636892a713e4f321013c96"
payload = {
    "actor": "unlocker.webunlocker",
    "proxy": {
        "country": "IL"
    },
    "input": {
        "url": url,
        "jsRender": {
            "enabled": True,
            "waitUntil":"domcontentloaded",
            "instructions":[{"wait": 7000}],
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
    for i in range(100):
      asyncio.run(main())
      print(i)
