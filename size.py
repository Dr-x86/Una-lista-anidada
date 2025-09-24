with open("urls.txt", 'r') as f:
    urls = f.readlines()
    print(f"Urls: {urls} \nLongitud: {len(urls)}")