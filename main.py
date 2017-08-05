#encoding = UTF-8
import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visit = set()
url = ''
queue.append(url)
cnt=0

while queue:
    url=queue.popleft()
