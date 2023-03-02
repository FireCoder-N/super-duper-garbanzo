import requests

while True:
    url = input("Enter a url or press enter to exit: ")
    
    if url == "":
        break

    try:
        headers = requests.get(url).headers
        for item in headers:
            print(item, ":  ", headers[item])
    except requests.exceptions.MissingSchema:
        print("Invalid url")
    
    print("\n")
