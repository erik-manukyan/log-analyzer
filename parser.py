# src/parser.py

import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'''^
    (?P<remote_host>\S+)\s+            # IP address
    (?:\S+\s+){3}                      # skip logname, country_code, user_ident
    

\[(?P<time_received>[^\]

]+)\]

\s+   # [dd/MM/yyyy:HH:mm:SS]
    "(?P<method>\S+)\s+                # "GET, "POST, etc.
    (?P<path>\S+)                      # /path/to/resource
    (?:\s+HTTP/(?P<version>\d\.\d))?"\s+
    (?P<status>\d{3})\s+               # 200, 404, etc.
    (?P<size>\S+)\s+                   # bytes sent or '-'
    "(?P<referer>[^"]*)"\s+            # "Referer" header
    "(?P<agent>[^"]*)"\s+              # "User-Agent" header
    (?P<resp_time>\d+)                 # response time in ms
    $''',
    re.VERBOSE
)

def parse_line(line: str) -> dict:
    """
    Parse a single log line. Return a dict of fields, or None if no match.
    """
    m = LOG_PATTERN.match(line)
    if not m:
        return None

    data = m.groupdict()
    # Parse timestamp (no timezone info)
    try:
        data['time'] = datetime.strptime(data['time_received'], '%d/%m/%Y:%H:%M:%S')
    except ValueError:
        data['time'] = None

    return data

def parse_file(path: str):
    """
    Generator: yield parsed dicts for each valid line in the log file.
    """
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for raw in f:
            entry = parse_line(raw.strip())
            if entry:
                yield entry

