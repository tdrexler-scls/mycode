#!/usr/bin/env python3

import http.client

def main():

    conn = http.client.HTTPConnection("localhost", 9021)

    conn.request('HEAD', '/')

    res = conn.getresponse()

    print(res.status, res.reason)

if __name__ == "__main__":
    main()
