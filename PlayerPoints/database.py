def mysql_run(cnx, sqlcontent):
    cursor = cnx.cursor()
    cursor.execute(sqlcontent)
    result = cursor.fetchall()
    cursor.close()
    return result