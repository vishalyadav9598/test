import re
def subdomain(domain, testdomain=()):
    regex = r"(https?:\/\/)?([w]{3}\.)?(\w*.\w*)([\/\w]*)"
    regex1 = r"\.?" + "(" + str(domain) + ".*)"
    result = re.sub(regex, '\\3', testdomain, re.MULTILINE | re.IGNORECASE)
    result = re.sub(regex1, "", result, 0, re.MULTILINE | re.IGNORECASE)
    if result:
        print(result)

subdomain('microsoft.com', (
    "https://blog.microsoft.com/test.html\n"
    "https://www.blog.microsoft.com/test/test\n"
    "https://test.microsoft.com\n"
    "https://www.microsoft.com")
          )
