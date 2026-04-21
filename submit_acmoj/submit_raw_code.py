#!/usr/bin/env python3
import os, requests, json, sys

def main():
    token = os.environ.get('ACMOJ_TOKEN')
    if not token:
        print('ACMOJ_TOKEN not set')
        sys.exit(1)
    api = 'https://acm.sjtu.edu.cn/OnlineJudge/api/v1'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'ACMOJ-Python-Client/2.2'
    }
    try:
        code_text = open('code','r',encoding='utf-8').read()
    except Exception as e:
        print('Failed to read code file:', e)
        sys.exit(1)
    data = {'language': 'git', 'code': code_text}
    r = requests.post(api + '/problem/1363/submit', headers=headers, data=data, timeout=20, proxies={'https': None, 'http': None})
    try:
        resp = r.json()
    except Exception:
        print(r.status_code, r.text)
        sys.exit(1)
    print(json.dumps(resp))

if __name__ == '__main__':
    main()
