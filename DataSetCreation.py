from pyspark.sql import SparkSession
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
