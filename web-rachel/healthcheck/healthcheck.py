#!/usr/bin/env python3
import requests

response = requests.get('https://beep-boop.ctf.ritsec.club/robots.txt')
if 'UlN7ZzMwbTJ0eV9kQHNoXyFzX2whZjN9' in response.text:
    exit(0)
exit(1)
