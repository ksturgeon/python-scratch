import jaydebeapi
jdbc_driver="org.apache.drill.jdbc.Driver"
driver_jar="/opt/mapr/drill/jars/jdbc-driver/drill-jdbc-all-1.11.0.jar"

print("connecting")
conn = jaydebeapi.connect(jdbc_driver,'jdbc:drill:zk=mapr-zk:5181/drill/61-demo-drillbits',["mapr", "maprmapr"],driver_jar)
print("connected")

curs = conn.cursor()
print("open cursor")
curs.execute("select * from cp.`employee.json` limit 10")

print("seleted")
curs.fetchall()
print("FETCHED")

curs.close()

