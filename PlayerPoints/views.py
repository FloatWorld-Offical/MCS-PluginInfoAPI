from django.shortcuts import render
from mysql import connector
from django.http import HttpResponse
import json
from . import database

def name(request, name):
    with open("./data/PlayerPoints/info.json", "r+", encoding="utf-8") as f:
        info = json.loads(f.read())
    cnx = connector.connect(host=info["database"]["host"], database=info["database"]["database"], user=info["database"]["user"], password=info["database"]["password"])
    try:
        # 玩家名 -> UUID
        sql1 = "SELECT * FROM playerpoints_username_cache WHERE username = '{}'".format(name)
        result1 = database.mysql_run(cnx, sql1)
        UUID = result1[0][0]
        # UUID -> points
        sql2 = "SELECT * FROM playerpoints_points WHERE uuid = '{}'".format(UUID)
        result2 = database.mysql_run(cnx, sql2)
        points = result2[0][2]
        cnx.close()
        return HttpResponse(
            json.dumps({"code": 0, "message": "Success", "data": {"name": name, "UUID": UUID, "points": points}}))
    except:
        cnx.close()
        return HttpResponse(json.dumps({"code": 1, "message": "Non-existent player"}))

