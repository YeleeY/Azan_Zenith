import requests

response = requests.get('http://api.aladhan.com/v1/timingsByCity/08-08-2023?city=Houston&country=United+States+of+America&method=2&school=1')

fajr = response.json()['data']['timings']['Fajr']
zuhr = response.json()['data']['timings']['Dhuhr']
asr = response.json()['data']['timings']['Asr']
magrib = response.json()['data']['timings']['Maghrib']
isha = response.json()['data']['timings']['Isha']
