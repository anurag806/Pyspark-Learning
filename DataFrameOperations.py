from pyspark.sql import SparkSession
from pyspark.sql.functions import col,when
"""spark=(SparkSession
       .builder
       .master('local[*]')
       .appName('Spark-App')
       .getOrCreate()
       );
csv_df=spark.read.csv("data/2015-12-12.csv",
                      header=True,
                      inferSchema=True)
csv_df.show();
print(csv_df.dtypes);
result=csv_df.select("ip_id").filter(csv_df.ip_id==25);
result.show();
spark.stop();"""
#use of Select
S1=(SparkSession.builder
    .master('local[*]')
    .appName('anurag')
    .getOrCreate());
read_data=S1.read.csv("data/pyspark_practice_customers.csv",
                      header=True,
                      inferSchema=True);
read_data.show();
'''res=read_data.select("*").filter((col("status")=="Active") | (col("experience")==4)).orderBy("salary");
res.show();
res=read_data.select("*").filter((col("salary")>70000)).show();
res1=read_data.select("*").filter((col("age")<30)).show();
res2=read_data.select("*").filter((col("salary")>60000)).show();
res3=read_data.select("*").filter((col("city")=="Kanpur")).show();
res4=read_data.select("*").filter((col("department")=="IT") & (col("status")=="Active")).show();
res5=read_data.select("*").filter((col("salary").between(50000,80000))).show();
res6=read_data.select("*").filter((col("experience")>=5) & (col("salary")>60000)).show();
res7=read_data.select("department","name","salary").show();
res8=read_data.select("city","name","salary","status").filter((col("status")=="Inactive")).show();
res9=read_data.select("*").orderBy("age").show();
res10=read_data.select("*").orderBy(col("salary").desc()).show();
res11=read_data.select("*").filter((col("department")=="Finance")).orderBy(col("salary").desc()).show();
res12=read_data.select("*").filter((col("city")).isin("Kanpur","Delhi")).show();
res13=read_data.select("*").filter((col("department")!="IT")).show();
res14=read_data.select("*").orderBy(col("salary").desc()).limit(5).show();
res15=read_data.select("name","salary","experience").filter((col("status")=="Active") & (col("experience")>5) & (col("salary")>60000)).orderBy(col("salary").desc()).show();'''
read_data.show();
#with column
re1=read_data.withColumn(
    "annual_salary",
    col("salary")*12
)
re1.show();
re2=read_data.withColumn(
    "bonus",
    col("salary")*0.10
)
re2.show();
re3=read_data.withColumn(
    "monthly_salary",
    col("salary")
)
re3.show();
re4 = read_data.withColumn(
    "level",
    when(col("experience") >= 5, "Experienced")
    .otherwise("Junior")
)

re4.show()
re5=read_data.withColumn(
    "salary_band",
    when(col("salary")>=80000, "High").when(col("salary")>=50000, "Medium").otherwise("Low")
)
re5.show()