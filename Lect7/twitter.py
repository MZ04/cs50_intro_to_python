import re

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
#To extract the username from the url we just need to delete the url before it
username = re.search(r"(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE)
#(?:...) -> Since I don't need to capture the "www" or "https" I impose to not capture it by using this syntax
if username:
    username=username.group(1)
#username=re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    print(f"hello, {username}")