from urllib.parse import urlparse
from urllib.parse import parse_qs


# parse in components
url = "http://example.com"
parsed = urlparse(url)

# parse qs
qs_dict = parse_qs(parsed.query)
