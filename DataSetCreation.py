from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
spark=(
    (SparkSession
     .builder
     .master("local[*]")
     .appName("an1"))
    .getOrCreate());
data=[
    (1,"anurag",2000),
    (2,"swati",3000),
    (3,"arya",4000),
]
column=["id","name","age"]
df=spark.createDataFrame(data,column);
df.show();
#reading data
csv_read=spark.read.csv("data/2015-12-12.csv",
                        header=True,
                        inferSchema=True);
csv_read.printSchema();
csv_read.show();
# showing only 10 items
csv_read.show(10);
# ordering
print(csv_read.columns);
csv_read.orderBy("ip_id").show(10);
csv_read.orderBy(desc("ip_id")).show(10);
