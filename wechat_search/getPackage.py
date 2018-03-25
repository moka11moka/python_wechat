#coding:utf8
import requests
import json

#create by guoxiang

#抓取快递100寄件个人信息

def getPackage(billNumber):
    company_url = 'https://m.kuaidi100.com/autonumber/auto?num='+billNumber
    company_name = json.loads(requests.get(company_url).text)[0]['comCode']
    bill_url = 'https://m.kuaidi100.com/query?type='+company_name+'&postid='+billNumber
    bill_infos = json.loads(requests.get(bill_url).text)['data']
    bill_information = '快递时间--到达位置:\n'
    for item in bill_infos:
        bill_information += item['time']+":"+item['context']+'\n'
    return '快递公司:'+transfer_company(company_name)+'\n'+bill_information

def transfer_company(company_name):
    if company_name == 'yuantong':
        return '圆通'
    elif company_name == 'shentong':
        return '申通'
    elif company_name == 'shunfeng':
        return '顺丰'
    elif company_name == 'jd':
        return '京东'
    elif company_name == 'zhongtong':
        return '中通'
    elif company_name == 'yunda':
        return '韵达'
    elif company_name == 'debangwuliu':
        return '德邦物流'
    else:
        return company_name

if __name__=='__main__':
    print(getPackage('3901942148081'))

