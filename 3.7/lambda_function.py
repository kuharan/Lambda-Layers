import pyodbc 
def lambda_handler(event,context):
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:xxx.database.windows.net,1433;Database=xxx;Uid=xxx;Pwd=xxx;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM xxx')

    for row in cursor:
        print(row)

lambda_handler(None,None)