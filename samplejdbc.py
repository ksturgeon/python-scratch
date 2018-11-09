import jaydebeapi
jdbc_driver="org.apache.drill.jdbc.Driver"

# This is the literal path for the driver on an edge/client node.  
# The relative path is $DRILL_HOME/jars/jdbc-driver/ - which is slightly different on a cluster node vs. and edge node 
driver_jar="/opt/mapr/drill/jars/jdbc-driver/drill-jdbc-all-1.11.0.jar"

print("connecting")
conn = jaydebeapi.connect(jdbc_driver,'jdbc:drill:drillbit=hostname:3010',["username", "password"],driver_jar)
print("connected")

curs = conn.cursor()
print("open cursor")
curs.execute("select * from cp.`employee.json` limit 10")

print("seleted")
curs.fetchall()
print("FETCHED")

curs.close()

