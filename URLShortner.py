import pyshorteners

url = input("Enter URL:\n")

print("URL after shortening: - ", pyshorteners.Shortener().tinyurl.short(url))
