import httpx
import asyncio
from datetime import datetime

async def fetch_hello(client, url, data, index):
    try:
        print(f"Sending data '{data}' to server {index+1}")
        response = await client.post(url, data=data)
        return response.text
    except httpx.RequestError as e:
        return f"An error occurred: {e}"

async def log_response(index, response_text):
    log_filename = f"server{index+1}.log"
    async with aiofiles.open(log_filename, 'a') as log_file:
        await log_file.write(f"{datetime.now()} - {response_text}\n")

async def main():
    urls = ["http://localhost:8080/hello", "http://localhost:8081/hello"]
    data = 'hi'
    
    async with httpx.AsyncClient(http2=True) as client:
        index = 0
        while True:
            url = urls[index]
            result = await fetch_hello(client, url, data, index)
            print(f"{datetime.now()} - Server {index + 1} response: {result}")
            
            await log_response(index, result)
            
            index = (index + 1) % len(urls)
            await asyncio.sleep(1)

if __name__ == "__main__":
    import aiofiles
    asyncio.run(main())

