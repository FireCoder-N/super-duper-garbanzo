import requests

while True:
    url = input("Enter a url or press enter to exit: ")
    
    if url == "":
        break

    try:
        cookies = requests.get(url).cookies
        headers = requests.get(url).headers

        print ("webserver:", headers['Server'])
        
        if "Set-Cookie" in headers.keys():
            print("Website uses the following cookies:")
            for cookie in cookies:
                print("\t", cookie, "expires in", cookie.expires)
                
    except requests.exceptions.MissingSchema:
        print("Invalid url")
    
    print("\n")
