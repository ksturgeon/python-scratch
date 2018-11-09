import jpype
import jaydebeapi
import os

driver_dir="/home/mapr/drill-jdbc/"
classpath = str.join(":", [driver_dir+name for name in os.listdir(driver_dir)])

args = "-Djava.class.path=%s" % classpath
jpype.startJVM(jpype.getDefaultJVMPath(), args)

conn = jaydebeapi.connect('com.mapr.drill.jdbc41.Driver', 'jdbc:drill:drillbit=10.10.72.78;AuthMech=MapRSASL')
curs = conn.cursor()
curs.execute("select * from sys.version")
curs.fetchall()
