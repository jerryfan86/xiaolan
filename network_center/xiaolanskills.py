# -*- coding: utf-8 -*-

import sys
import os
import json
import demjson
import requests
import httplib
import urllib
import urllib2
import hashlib
import base64
import time
sys.path.append('/home/pi/xiaolan/')
from speech_center.conversation import dialogue
from display_center.display import screen
import setting

class skills(object):

    def __init__(self):
        pass
    def skillReq(self, url, intent, slots, intentdict, converid):

        sk = skills()
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': intent,
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['clienttype'],
                    'ClientId': setting.setting()['main_setting']['clientid']
                },
                'ConversationInfo': {
                    'ConversationId': converid,
                    'ShouldHandlerSkill': intentdict['skill'],
                    'SkillShouldHandler': intent,
                    'SkillAwakenKeyword': intentdict['keyword'],
                    'SendToSkillInfo': {
                        'Intent': intent,
                        'Text': intentdict['text'],
                        'Slots': slots
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['clientid'],
                'States': {
                    'ClientStates': ['serviceing'],
                    'NluStates': ['working'],
                    'SttStates': ['working'],
                    'TtsStates': ['emptyling']
                },
                'Commands': {
                    'ClientCommands': ['service for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(url,
                          data=json.dumps(data))
        sk.command(r.json())
    
    def skillTryLive(self, url, skillname):
        
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.skill.tryalive',
                    'ServerShouldHandler': 'tryskillalive'
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['clienttype'],
                    'ClientId': setting.setting()['main_setting']['clientid']
                },
                'ConversationInfo': {
                    'ConversationId': None,
                    'ShouldHandlerSkill': skillname,
                    'SkillShouldHandler': None,
                    'SkillAwakenKeyword': None,
                    'SendToSkillInfo': {
                        'Intent': None,
                        'Text': None,
                        'Slots': None
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['clientid'],
                'States': {
                    'ClientStates': ['serviceing'],
                    'NluStates': ['emptyling'],
                    'SttStates': ['emptying'],
                    'TtsStates': ['emptyling']
                },
                'Commands': {
                    'ClientCommands': ['service for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(url,
                          data=json.dumps(data))
        json = r.json()
        return json['state']
        
    def command(self, json):

        s = screen()
        d = dialogue()
        m = music()
        commands = json['commands'][0]
        if commands == 'Ask':
            respones = d.ask(json['commands'][1]['text'], json['commands'][1]['slot'], json['commands'][1]['recordtype'])
            r = requests.post(url,
                              data=json.dumps({'states': 'ASKturnback', 'key': 'xiaolanserverpasswordYYH', 'askturn': respones}))
        elif commands == 'MusicPlay':
            musicurl = json['commands'][1]
            m.download(musicurl)
            speaker.play(json['commands'][2])
        elif commands == 'MusicStop':
            speaker.stop()
        elif comamnds == '
        
