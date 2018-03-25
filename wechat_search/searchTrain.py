#用来查询火车站余票信息
import requests
import re
'''
requests解析的结果
@拼音缩写三位|站点名称|编码|拼音|拼音缩写|序号
使用方式:dgz+上海+北京+2018-03-25 （其中可选车型d动车，g高铁,k快速,t特快，z直达）
'''
def getTickect(query_tarin):
    '''按照 '''
    infolist = query_tarin.split('+')
    header = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36"
        }
    requests.packages.urllib3.disable_warnings()
    train_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050'
    stations = dict(re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', requests.get(train_url).text))
    infos = {
        'option': infolist[0],
        'from_stat': infolist[1],
        'to_stat': infolist[2],
        'date': infolist[3]
    }
    from_stat = stations[infos['from_stat']]
    to_stat = stations[infos['to_stat']]
    date = infos['date']
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_stat, to_stat)
    ticket_infos = requests.get(url, verify=False)
    requests.packages.urllib3.disable_warnings()
    ticket_infos = ticket_infos.json()['data']['result']
    for ticket_info in ticket_infos:
        from_stat_no = to_stat_no = ""
        info = ticket_info.split('|')
        train_no, train_code = info[2], info[3]
        #print(info[4],info[5])
        no_url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no={}&from_station_telecode={}&to_station_telecode={}&depart_date={}'.format(train_no,info[4],info[5],date)
        train_infos = requests.get(no_url, verify=False).json()['data']['data']

        requests.packages.urllib3.disable_warnings()
        for train_info in train_infos:
            if infos['from_stat'] in train_info['station_name']:
                from_stat_no = train_info['station_no']
            if infos['to_stat'] in train_info['station_name']:
                to_stat_no = train_info['station_no']
        price_url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no={}&from_station_no={}&to_station_no={}&seat_types={}&train_date={}'.format(train_no, from_stat_no,to_stat_no,info[35],date)
        price_infos = requests.get(price_url, verify=False).json()['data']
        requests.packages.urllib3.disable_warnings()
        if 'WZ' in price_infos.keys():
            price_infos = price_infos['WZ']
        else:
            price_infos = ""
        details = train_code+'\t'+infos['from_stat']+'\t'+infos['to_stat']+'\t'+'--'.join([info[8],info[9]])+'\t'+info[10]+'\t'+price_infos
        print(details)
getTickect('dgz+上海+北京+2018-03-27')





















