# Use the JDBC connection library for python
import jaydebeapi

# This is a sample piece of code showing how to use the JDBC drivers to connect to the drill cluster

def connect_todrill_jaybebeapi():
	# Have to give it the driver class name:
	jdbc_driver="org.apache.drill.jdbc.Driver"

	# Driver jar location - if this is in the classpath, we don't need to set it.
	# Also - this jar file location is different between a client node and a cluster node
	# Since $DRILL_HOME is different - $DRILL_HOME/jars/jdbc-driver/...jar
	driver_jar="/opt/mapr/drill/jars/jdbc-driver/drill-jdbc-all-1.11.0.jar"

	print("=============================")

	#  We'll try to use similar nomenclature:
	drill  =  jaybebeapi.connect(jdbc_driver, 'jdbc:drill:zk=l01nsvl-dcmpr01.sdqa.lpl.com:5181,l01nsvl-dcmpr02.sdqa.lpl.com:5181,l01nsvl-dcmpr03.sdqa.lpl.com:5181/drill/LDQALake.lpl.com-drillbits', ["username", "password"], driver_jar)
	print("connected")
	return 1

connect_todrill_jaybebeapi()

