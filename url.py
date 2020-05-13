from urllib.parse import parse_qs
from urllib.parse import urlparse
from urllib.parse import unquote


# parse in components
url = "http://example.com"
parsed = urlparse(url)

# parse qs
qs_dict = parse_qs(parsed.query)

# decode data that is UTF-8 encoded bytes escaped with URL quoting
# unquote decoding from percent-encoded data to UTF-8 bytes and then to text,
url = "https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA4MDk5MTA4OQ%3D%3D%26mid%3D2651267874%26idx%3D2%26sn%3D700236d4946ac47832cfb9ff44ecd5b1%26chksm%3D8468453cb31fcc2a9d2731414c6f580ba38297a5df21cc30813ff20b378e636084b3fd6caa48"
url = unquote(url)
