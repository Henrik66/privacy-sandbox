# Importing asyncio for concurrent networking
import asyncio

# Importing aiohttp for HTTP requests
import aiohttp

# Importing subprocess to call OS binaries (e.g. wget)
import subprocess

# URL for the Tranco list
tranco='https://tranco-list.eu/download/daily/tranco_58XXN-1m.csv.zip'

# Number of concurrent networking requests
num_of_requests = 10000

# Declare a global semaphore with a limit of num_of_requests
semaphore = asyncio.Semaphore(num_of_requests)

# Function to download a url and save it to a file if it is a json content
async def fetch_and_save(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            json_url = f"https://{url}/.well-known/privacy-sandbox-attestations.json"
            try:
                async with session.get(json_url) as response:
                    if response.status == 200:
                        content = await response.read()
                        if chr(content[0])=='{':
                            with open(url+'.json', 'wb') as file:
                                print(url)
                                file.write(content)
            except Exception:
                pass

async def main():
    # Use wget to download the Tranco list
    subprocess.run(["wget", tranco])

    # Uncompress
    subprocess.run(["unzip", '-o', '*.zip'])

    with open("top-1m.csv", "r") as f:
        tasks = [fetch_and_save(line.split(",")[1].strip()) for line in f]
        await asyncio.gather(*tasks)

asyncio.run(main())
