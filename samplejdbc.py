import jaydebeapi
jdbc_driver="org.apache.drill.jdbc.Driver"

# This is the literal path for the driver on an edge/client node.  
# The relative path is $DRILL_HOME/jars/jdbc-driver/ - which is slightly different on a cluster node vs. and edge node 
driver_jar="/opt/mapr/drill/drill-1.12.0/jars/jdbc-driver/drill-jdbc-all-1.12.0-mapr.jar"

print("connecting")
conn = jaydebeapi.connect(jdbc_driver,'jdbc:drill:drillbit=10.250.101.72:31010',["mapr", "maprmapr"],driver_jar)
print("connected")

curs = conn.cursor()
print("open cursor")
curs.execute("select * from cp.`employee.json` limit 10")

print("seleted")
curs.fetchall()
print("FETCHED")

print curs.description

curs.close()

