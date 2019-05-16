import jpype
import jaydebeapi
import os

driver_dir="/opt/mapr/drill/lib/"
classpath = str.join(":", [driver_dir+name for name in os.listdir(driver_dir)])

args = "-Djava.class.path=%s" % classpath
jpype.startJVM(jpype.getDefaultJVMPath(), args)

conn = jaydebeapi.connect('com.mapr.drill.jdbc41.Driver', 'jdbc:drill:drillbit=10.250.101.13:31010',["mapr","maprmapr"])
curs = conn.cursor()
#curs.execute("select * from sys.version")
curs.execute("select * from cp.`employee.json` limit 10")
curs.fetchall()
print(curs.description)
