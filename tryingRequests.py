import requests
import time

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

start_time = time.perf_counter()
for url in URLS:
    try:
        
        response = requests.get(url)
        response.raise_for_status()
    except:
        print(f"Error code: {response.status_code}")
    else:
        print("Success!")
end_time = time.perf_counter()

print(f"Time taken: {end_time - start_time:.2f} seconds")



