import pyshorteners
url=input("Enter URL = ")

s=pyshorteners.Shortener()
print("Your extended URL is -> ",s.tinyurl.expand(url))