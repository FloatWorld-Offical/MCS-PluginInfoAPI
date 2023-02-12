from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mysql import connector
from django.http import HttpResponse
import json
from . import database
import random
import datetime

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def generatekey():
    list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key = ""
    for i in range(4):
        for z in range(8):
            key += random.choice(list)
        key += "-"
    key = key.rstrip("-")
    return key

@csrf_exempt
def check(request, plugin):
    with open("./data/PluginCheck/info.json", "r+", encoding="utf-8") as f:
        info = json.loads(f.read())
    key = request.POST['key']
    cnx = connector.connect(host=info["database"]["host"], database=info["database"]["database"],
                            user=info["database"]["user"], password=info["database"]["password"])
    ip = get_client_ip(request)
    try:
        # key -> 剩余天数
        sql1 = "SELECT {}_time FROM keydays WHERE checkkey = '{}' and {}_ip = '{}'".format(plugin, key, plugin, ip)
        result1 = int(database.mysql_run(cnx, sql1)[0][0])
        cnx.close()
        if result1 >= datetime.datetime.today().timestamp():
            return HttpResponse(
                json.dumps({"code": 0, "message": "Success"}))
        else:
            return HttpResponse(
                json.dumps({"code": 1, "message": "Expired"}))
    except:
        cnx.close()
        return HttpResponse(json.dumps({"code": 1, "message": "Non-existent key or Error ip"}))

def new(request, qq, plugin, length):
    with open("./data/PluginCheck/info.json", "r+", encoding="utf-8") as f:
        info = json.loads(f.read())
    cnx = connector.connect(host=info["database"]["host"], database=info["database"]["database"],
                            user=info["database"]["user"], password=info["database"]["password"])
    length = int(length)
    try:
        sql1 = "SELECT * FROM keydays WHERE qq = '{}'".format(qq)
        result1 = database.mysql_run(cnx, sql1)
        date = int(result1[0][info["plugin_index"][plugin]])
        cnx.commit()
        if result1 == 1:
            key = generatekey()
            time = int(datetime.datetime.today().timestamp()) + 86400*30*length
            sql2_2 = "INSERT INTO keydays (checkkey, qq, {}, {}_time) VALUES ('{}', '{}', 1, '{}');".format(plugin,
                                                                                                            plugin, key,
                                                                                                            qq,
                                                                                                            str(time))
            cur = cnx.cursor()
            cur.execute(sql2_2)
            cnx.commit()
            cur.close()
        else:
            if date >= datetime.datetime.today().timestamp():
                time = date + 86400*30*length
            else:
                time = int(datetime.datetime.today().timestamp()) + 86400*30*length
            sql2_1 = "UPDATE keydays SET {} = 1, {}_time = {} WHERE qq = {};".format(plugin, plugin, str(time), qq)
            cur = cnx.cursor()
            cur.execute(sql2_1)
            cnx.commit()
            cur.close()
            sql3 = "SELECT checkkey FROM keydays WHERE qq = '{}'".format(qq)
            key = database.mysql_run(cnx, sql3)[0][0]
        cnx.close()
        return HttpResponse(
            json.dumps({"code": 0, "message": "Success", "data": {"key": key, "Plugin": plugin, "time": datetime.datetime.utcfromtimestamp(time).strftime("%Y-%m-%d")}}))
    except:
        return HttpResponse(
            json.dumps({"code": 1, "message": "Error Parameter"}))

def bind(request, qq, plugin, ip):
    with open("./data/PluginCheck/info.json", "r+", encoding="utf-8") as f:
        info = json.loads(f.read())
    cnx = connector.connect(host=info["database"]["host"], database=info["database"]["database"],
                            user=info["database"]["user"], password=info["database"]["password"])
    try:
        sql2_1 = "UPDATE keydays SET {}_ip = '{}' WHERE qq = {};".format(plugin, ip, qq)
        cur = cnx.cursor()
        cur.execute(sql2_1)
        cnx.commit()
        cur.close()
        cnx.close()
        return HttpResponse(
            json.dumps({"code": 0, "message": "Success", "data": {"QQ": qq, "plugin": plugin, "IP": ip}}))
    except:
        return HttpResponse(
            json.dumps({"code": 1, "message": "Error Parameter"}))
