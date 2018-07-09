# -*- coding: utf-8 -*-

sys.path.append('/home/pi/xiaolan/')
import setting

def dictcity():
    return {
            'same_means': [
                '北京', '中山', '上海', '广州', '长春', '天津', '重庆', '哈尔滨', '西安', '武汉',
                '沈阳', '南京', '成都', '石家庄', '大连', '齐齐哈尔', '南昌', '郑州', '兰州', '唐山',
                '鞍山', '徐州', '济南', '长沙', '乌鲁木齐', '太原', '抚顺', '杭州', '青岛', 
                '贵阳', '包头', '吉林', '福州', '淄博', '昆明', '邯郸', '保定', '张家口', '大同',
                '呼和浩特', '本溪', '丹东', '锦州','阜新', '辽阳', '鸡西', '鹤岗', '大庆',	'伊春',
                '佳木斯市',	'牡丹江', '无锡', '常州', '苏州','宁波', '合肥', '淮南', '淮北', '厦门',
                '枣庄', '烟台', '潍坊', '泰安', '临沂', '开封', '洛阳', '平顶山市', '安阳', '新乡', '焦作市', '黄石',
                '襄樊市', '荆州', '株洲', '湘潭', '衡阳', '深圳',' 汕头', '湛江', '南宁', '柳州', '西宁'
            ],
           'dict': [
                '北京市', '中山市', '上海市', '广州市', '长春市', '天津市', '重庆市', '哈尔滨市', '西安市', '武汉市',
                '沈阳市', '南京市', '成都市', '石家庄市', '大连市', '齐齐哈尔市', '南昌市', '郑州市', '兰州市', '唐山市',
                '鞍山市', '徐州市', '济南市', '长沙市', '乌鲁木齐市', '太原市', '抚顺市', '杭州市', '青岛市', 
                '贵阳市', '包头市', '吉林市', '福州市', '淄博市', '昆明市', '邯郸市', '保定市', '张家口市', '大同市',
                '呼和浩特市', '本溪市', '丹东市', '锦州市','阜新市', '辽阳市', '鸡西市', '鹤岗市', '大庆市',	'伊春市',
                '佳木斯市',	'牡丹江市', '无锡市', '常州市', '苏州市','宁波市', '合肥市', '淮南市', '安徽省淮北市', '福建省厦门市',
                '枣庄市', '烟台市', '潍坊市', '泰安市', '临沂市', '开封市', '洛阳市', '平顶山市', '安阳市', '新乡市', '焦作市', '黄石市',
                '襄樊市', '荆州市', '株洲市', '湘潭市', '衡阳市', '深圳市',' 汕头市', '湛江市', '南宁市', '柳州市', '西宁市'
           ]
    }

def dicthasscortolmode():
    return {
            'same_means': [
                '开启', '', '摆风'
            ],
            'dict': [
                '打开', '关闭', '摇头', '自动化设置', '场景设置', '设置场景', '设置自动化', '风速', '静音', '风类'
            ]
    }

def dictnewstype():
    return {
        'same_means': [
            '', '', ''
        ],
        'dict': [
            'keji', 'guonei', 'guoji'
        ]
        }

def dicthassdevice():
    return {
        'same_means': [],
        'dict': [
            '电视', '风扇', '盒子', '机顶盒', '灯'
        ]
    }

def GetSlotsDict():

    data = {
        'ClientEvent': {
            'Header': {
                'NameSpace': 'xiaolan.client.commands.slotsdict.get',
                'TimeStamp': int(time.time()),
                 'RequestsId': '7636',
                 'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                 'ClientId': setting.setting()['main_setting']['ClientId']
            },
            'ConversationInfo': {
                'ConversationId': None,
                'ShouldHandlerSkill': None,
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
                'NluStates': ['working'],
                'SttStates': ['emptying'],
                'TtsStates': ['emptying']
            },
            'Commands': {
                'ClientCommands': ['service for user'],
                'elseCommands': []
            }
        }
    }
    r = requests.post(setting.setting()['main_setting']['url'],
                      data=data)

