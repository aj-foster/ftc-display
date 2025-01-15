#!/usr/bin/env python3

import requests
import subprocess

# Change the following to match your setup:
SCORING_ADDRESS = "10.10.10.10"
FIELD_NUMBER = 1

def get_event_codes():
    response = requests.get(f"http://{SCORING_ADDRESS}/api/v1/events")
    if response.status_code != 200: exit(1)
    return response.json()['eventCodes']

def get_event(code):
    response = requests.get(f"http://{SCORING_ADDRESS}/api/v1/events/{code}")
    if response.status_code != 200: exit(1)
    return response.json()

def get_current_event():
    current_event = None

    for code in get_event_codes():
        event = get_event(code)
        if event['status'] == 'Archived': continue
        current_event = event

    return current_event

event = get_current_event()
if event is None: exit(1)
print(event)

code = event['eventCode']
fieldCount = event['fieldCount']

field = min(FIELD_NUMBER, fieldCount)
display_url = f"http://{SCORING_ADDRESS}/event/{code}/display/?type=field&bindToField={field}&scoringBarLocation=bottom&allianceOrientation=standard&liveScores=false&mute=false&muteRandomizationResults=true&fieldStyleTimer=true&overlay=false&overlayColor=%2300FF00&allianceSelectionStyle=classic&awardsStyle=overlay&dualDivisionRankingStyle=sideBySide&rankingsFontSize=larger&rankingsShowQR=false&showMeetRankings=false&rankingsAllTeams=true&name=Field+{code}"

subprocess.Popen(["xdotool", "mousemove", "960", "540", "sleep", "60", "click", "1"])
subprocess.run(["chromium-browser", "--start-fullscreen", "--app", display_url])
