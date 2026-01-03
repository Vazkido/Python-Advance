import re

urls = ''' 
https://www.google.com
http://coreyms.com.ng
https://youtube.com
https://www.nasa.gov
It should not detect this www.test.com
'''

# pattern = re.compile(r"(http|https)://\d?{3}[.]") Failed
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)(\.\w+)?")

matches = pattern.finditer(urls)
for match in matches:
    print(match)