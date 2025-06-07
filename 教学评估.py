from bs4 import BeautifulSoup
import requests
import random
import ddddocr


class urp():
    def __init__(self,account,password):
        self.x = requests.session()
        self.account = account
        self.password = password
        self.login()

    #登录
    def login(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
            "Referer": "http://192.168.16.207:9001/loginAction.do",
            "Origin": "http://192.168.16.207:9001",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        ocr = ddddocr.DdddOcr(show_ad=False)
        random_param = random.random()
        captcha_url = f"http://192.168.16.207:9001/validateCodeAction.do?random={random_param}"
        captcha_response = self.x.get(captcha_url)
        with open('captcha.jpg', 'wb') as f:
            f.write(captcha_response.content)
            f.close()
        with open('captcha.jpg', 'rb') as f:
            yzmcontent = f.read()
            yzm = ocr.classification(yzmcontent)
            f.close()
        data = {
            "zjh1": "",
            "tips": "",
            "lx": "",
            "evalue": "",
            "eflag": "",
            "fs": "",
            "dzslh": "",
            "zjh": self.account,
            "mm": self.password,
            "v_yzm": yzm
        }
        self.x.post("http://192.168.16.207:9001/loginAction.do", data=data, headers=header)


    #发送第一条信息
    def ask_list(self):
        url = f"http://192.168.16.207:9001/jxpgXsAction.do?oper=listWj&yzxh={self.account}"
        headers = {
            'Host': '192.168.16.207:9001',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '235',
            'Origin': 'http://192.168.16.207:9001',
            'Connection': 'keep-alive',
            'Referer': f'http://192.168.16.207:9001/jxpgXsAction.do?oper=listWj&yzxh={self.account}',
            'Upgrade-Insecure-Requests': '1',
            'Priority': 'u=4',
        }
        params = {
            'oper': 'listWj',
            'yzxh': self.account,
        }
        pg_lists = self.x.get(url, params=params,headers=headers, verify=False)
        return pg_lists.text
    #发送第二条信息
    def ask_wjshow(self,wjbm,bpr,pgnr):
        url = 'http://192.168.16.207:9001/jxpgXsAction.do'
        data = {
            "wjbm": wjbm,
            "bpr": bpr,
            "pgnr": pgnr,
            "oper" : "wjShow"
        }
        headers = {
            'Host': '192.168.16.207:9001',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://192.168.16.207:9001',
            'Connection': 'keep-alive',
            'Referer': f'http://192.168.16.207:9001/jxpgXsAction.do?oper=listWj&yzxh={self.account}',
            'Upgrade-Insecure-Requests': '1',
            'Priority': 'u=4'
        }
        self.x.post(url,data=data, headers=headers)
    #发送第三条信息
    def send_pg(self,wjbm, bpr, pgnr):
        url = 'http://192.168.16.207:9001/jxpgXsAction.do?oper=wjpg'
        headers = {
            'Host': '192.168.16.207:9001',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://192.168.16.207:9001',
            'Connection': 'keep-alive',
            'Referer': 'http://192.168.16.207:9001/jxpgXsAction.do',
            'Upgrade-Insecure-Requests': '1',
            'Priority': 'u=4'
        }
        data = {
            'wjbm': wjbm,
            'bpr': bpr,
            'pgnr': pgnr,
            'xumanyzg': 'zg',
            'wjbz': '',
            '0000000005': '20_1',
            '0000000007': '0_0',
            '0000000008': '0_0',
            '0000000011': '0_0',
            '0000000012': '0_0',
            '0000000013': '0_0',
            '0000000018': '5_0.9',
            '0000000019': '0_0',
            '0000000014': '0_0',
            '0000000006': '20_1',
            '0000000002': '5_1',
            '0000000003': '10_1',
            '0000000017': '10_1',
            '0000000020': '20_1',
            '0000000015': '5_1',
            '0000000016': '5_0.7',
            'zgpj': ''
        }
        self.x.post(url, data=data, headers=headers)
    #获取题目列表
    def ask_pg_list(self,pg_lists):
        soup = BeautifulSoup(pg_lists,'lxml')
        #找所有没评价的课程
        list = []
        for tr in soup.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) >= 4 and tds[3].get_text(strip=True) == '否':
                # 找到未评教的课程
                img_tag = tr.find('img')
                if img_tag and 'name' in img_tag.attrs:
                    name_field = img_tag['name']
                    parts = name_field.split('#@')
                    if len(parts) >= 6:
                        wjbm = parts[0]
                        bpr = parts[1]
                        pgnr = parts[5]
                        teacher_name = parts[2]
                        course_name = parts[4]
                        print(f"未评课程：{course_name}，教师：{teacher_name}")
                        entry = {
                            'wjbm':wjbm,
                            'bpr':bpr,
                            'pgnr':pgnr
                        }
                        list.append(entry)
        return list


#这里填上你的urp账号密码
account = ''
password = ''

urp = urp(account,password)

html = urp.ask_list()
list = urp.ask_pg_list(html)

for i in list:
    urp.ask_list()
    wjbm, bpr, pgnr = i.get('wjbm'), i.get('bpr'), i.get('pgnr')
    urp.ask_wjshow(wjbm, bpr, pgnr)
    urp.send_pg(wjbm, bpr, pgnr)