from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import time
from configparser import ConfigParser

conf_file_path = "/home/bach/Lakehouse/making/realtime_data_processing/"
conf_file_name = conf_file_path + "stream_app.conf"
config_obj = ConfigParser()
config_read_obj = config_obj.read(conf_file_name)

kafka_host_name = config_obj.get('kafka', 'host')
kafka_port_no = config_obj.get('kafka', 'port_no')
input_kafka_topic_name = config_obj.get('kafka', 'input_topic_name')
output_kafka_topic_name = config_obj.get('kafka', 'output_topic_name')
kafka_bootstrap_servers = kafka_host_name + ':' + kafka_port_no

mysql_host_name = config_obj.get('mysql', 'host')
mysql_port_no = config_obj.get('mysql', 'port_no')
mysql_user_name = config_obj.get('mysql', 'username')
mysql_password = config_obj.get('mysql', 'password')
mysql_database_name = config_obj.get('mysql', 'db_name')
mysql_driver = config_obj.get('mysql', 'driver')

mysql_byname_table_name = config_obj.get('mysql', 'mysql_byname_tbl')
mysql_bygender_table_name = config_obj.get('mysql', 'mysql_bygender_tbl')
mysql_bymajors_table_name = config_obj.get('mysql', 'mysql_bymajors_tbl')
mysql_bydepartment_table_name = config_obj.get('mysql', 'mysql_bydepartment_tbl')
mysql_byyearstudy_table_name = config_obj.get('mysql', 'mysql_byyearstudy_tbl')

mysql_jdbc_url = "jdbc:mysql://" + mysql_host_name + ":" + mysql_port_no + "/" + mysql_database_name

db_properties = {}
db_properties['user'] = mysql_user_name
db_properties['password'] = mysql_password
db_properties['driver'] = mysql_driver

def save_to_mysql_table(current_df, epoc_id, mysql_table_name):

    print("Printing MySQL table name: " + mysql_table_name)

    mysql_jdbc_url = "jdbc:mysql://" + mysql_host_name + ":" + str(mysql_port_no) + "/" + mysql_database_name

    current_df = current_df.withColumn('batch_no', lit(epoc_id))

    current_df.write.jdbc(url = mysql_jdbc_url,
                  table = mysql_table_name,
                  mode = 'append',
                  properties = db_properties)

    print("Exit out of save to MySQL table function")

if __name__ == "__main__":
    print("Welcome to Lakehouse Platform !!!")
    print("Real-Time Data Processing Application Started ...")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    spark = SparkSession \
        .builder \
        .appName("Lakehouse Platform For Sports Data Analytics") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    runner_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
        .option("subscribe", input_kafka_topic_name) \
        .option("startingOffsets", "latest") \
        .load()
    print("Printing Schema from Apache Kafka: ")
    runner_df.printSchema()

    runner_df1 = runner_df.selectExpr("CAST(value AS STRING)", "timestamp")

    runner_schema = StructType() \
        .add("run_id", StringType()) \
        .add("student_id", StringType()) \
        .add("name", StringType()) \
        .add("gender", StringType()) \
        .add("org_name", StringType()) \
        .add("org_name_child", StringType()) \
        .add("year_study", StringType()) \
        .add("average_speed", StringType()) \
        .add("max_speed", StringType()) \
        .add("average_heartrate", StringType()) \
        .add("max_heartrate", StringType()) \
        .add("distance", StringType()) \
        .add("elapsed_time", StringType()) \
        .add("moving_time", StringType()) \
        .add("total_elevation_gain", StringType()) \
        .add("elev_high", StringType()) \
        .add("type", StringType()) \
        .add("start_date_local", StringType()) \
        .add("kudos_count", StringType())
    
    runner_df2 = runner_df1\
        .select(from_json(col("value"), runner_schema)\
        .alias("runner"), "timestamp")

    runner_df3 = runner_df2.select("runner.*", "timestamp")

    runner_df3 = runner_df3.withColumn("partition_date", to_date("start_date_local"))
    runner_df3 = runner_df3.withColumn("partition_hour", hour(to_timestamp("start_date_local", 'yyyy-MM-dd HH:mm:ss')))

    runner_agg_write_stream_pre = runner_df3 \
        .writeStream \
        .trigger(processingTime='10 seconds') \
        .outputMode("update") \
        .option("truncate", "false")\
        .format("console") \
        .start()

    runner_raw_hdfs = runner_df3.writeStream \
        .trigger(processingTime='10 seconds') \
        .format("parquet") \
        .option("path", "hdfs://localhost:9000/Lakehouse/Bronze") \
        .option("checkpointLocation", "hdfs://localhost:9000/Lakehouse/Checkpoint_Bronze") \
        .partitionBy("partition_date", "partition_hour") \
        .start()
    
    print("Printing Schema of Bronze Layer: ")
    runner_df3.printSchema()

    columns_to_drop = ["run_id", "average_heartrate", "max_heartrate"]
    runner_del_silver = runner_df3.drop(*columns_to_drop)  

    runner_cleaned_hdfs = runner_del_silver.writeStream \
        .trigger(processingTime='10 seconds') \
        .format("parquet") \
        .option("path", "hdfs://localhost:9000/Lakehouse/Silver") \
        .option("checkpointLocation", "hdfs://localhost:9000/Lakehouse/Silver") \
        .partitionBy("partition_date", "partition_hour") \
        .start()
    
    print("Printing Schema of Silver Layer: ")
    runner_del_silver.printSchema()

    runner_df4 = runner_del_silver.groupBy("year_study") \
        .agg({'distance': 'sum'}) \
        .select("year_study", col("sum(distance)") \
        .alias("total_distance"))

    print("Printing Schema of total distance by Course: ")
    runner_df4.printSchema()

    runner_df4 \
    .writeStream \
    .trigger(processingTime='10 seconds') \
    .outputMode("update") \
    .foreachBatch(lambda current_df, epoc_id: save_to_mysql_table(current_df, epoc_id, mysql_byyearstudy_table_name)) \
    .start()

    runner_df5 = runner_del_silver.groupBy("org_name") \
        .agg({'distance': 'sum'}) \
        .select("org_name", col("sum(distance)") \
        .alias("total_distance"))

    print("Printing Schema of total distance by Majors: ")
    runner_df5.printSchema()

    runner_df5 \
    .writeStream \
    .trigger(processingTime='10 seconds') \
    .outputMode("update") \
    .foreachBatch(lambda current_df, epoc_id: save_to_mysql_table(current_df, epoc_id, mysql_bymajors_table_name)) \
    .start()

    runner_df6 = runner_del_silver.groupBy("student_id", "name") \
        .agg({'distance': 'sum'}) \
        .select("student_id", "name", col("sum(distance)") \
        .alias("total_distance"))
    
    print("Printing Schema of total distance by Name: ")
    runner_df6.printSchema()

    runner_df6 \
    .writeStream \
    .trigger(processingTime='10 seconds') \
    .outputMode("update") \
    .foreachBatch(lambda current_df, epoc_id: save_to_mysql_table(current_df, epoc_id, mysql_byname_table_name)) \
    .start()

    runner_df7 = runner_del_silver.groupBy("gender") \
    .agg({'distance': 'sum'}) \
    .select("gender", col("sum(distance)") \
    .alias("total_distance"))

    print("Printing Schema of total distance by Gender: ")
    runner_df7.printSchema()

    runner_df7 \
    .writeStream \
    .trigger(processingTime='10 seconds') \
    .outputMode("update") \
    .foreachBatch(lambda current_df, epoc_id: save_to_mysql_table(current_df, epoc_id, mysql_bygender_table_name)) \
    .start()

    runner_df8 = runner_del_silver.groupBy("org_name_child") \
    .agg({'distance': 'sum'}) \
    .select("org_name_child", col("sum(distance)") \
    .alias("total_distance"))

    print("Printing Schema of total distance by Department: ")
    runner_df8.printSchema()

    runner_df8 \
    .writeStream \
    .trigger(processingTime='10 seconds') \
    .outputMode("update") \
    .foreachBatch(lambda current_df, epoc_id: save_to_mysql_table(current_df, epoc_id, mysql_bydepartment_table_name)) \
    .start()

    runner_agg_write_stream = runner_df7 \
        .writeStream \
        .trigger(processingTime='10 seconds') \
        .outputMode("update") \
        .option("truncate", "false")\
        .format("console") \
        .start()

    runner_agg_write_stream.awaitTermination()

    print("Real-Time Data Processing Application Completed.")
