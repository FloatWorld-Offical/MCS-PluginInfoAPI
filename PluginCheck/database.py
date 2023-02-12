def mysql_run(cnx, sqlcontent):
    cur = cnx.cursor()
    cur.execute(sqlcontent)
    try:
        result = cur.fetchall()
        result1 = result[0][0]
    except:
        result = 1
    cur.close()
    return result