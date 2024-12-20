# Databricks notebook source
# DBTITLE 1,fetch the volume_folder value
dbutils.widgets.text("volume_folder", "")
volume_folder = dbutils.widgets.get("volume_folder")

# COMMAND ----------

# DBTITLE 1,install awscli
# MAGIC %pip install awscli

# COMMAND ----------

# DBTITLE 1,set the tmp dir and download the data from aws s3
# MAGIC %sh
# MAGIC mkdir -p /tmp/data
# MAGIC aws s3 cp --no-progress --no-sign-request s3://amazon-visual-anomaly/VisA_20220922.tar /tmp

# COMMAND ----------

# DBTITLE 1,unzip the images
# MAGIC %sh
# MAGIC mkdir -p /tmp/data
# MAGIC tar xf /tmp/VisA_20220922.tar --no-same-owner -C /tmp/data/ 

# COMMAND ----------

# MAGIC %md
# MAGIC # Copy data to the volume

# COMMAND ----------

# DBTITLE 1,chmod permissions
# MAGIC %sh
# MAGIC chmod -R 777 /tmp/data/pcb1/Data/Images/

# COMMAND ----------

# DBTITLE 1,recreate images dir required for demo
dbutils.fs.rm(volume_folder + "/images", recurse=True)
dbutils.fs.mkdirs(volume_folder + "/images")

# COMMAND ----------

# DBTITLE 1,copy images data to volume
# MAGIC %sh
# MAGIC cp -r /tmp/data/pcb1/Data/Images/* /Volumes/main__build/dbdemos_computer_vision_dl/pcb_training_data/images/

# COMMAND ----------

# DBTITLE 1,recreate labels dir required for demo
dbutils.fs.rm(volume_folder + "/labels", recurse=True)
dbutils.fs.mkdirs(volume_folder + "/labels")

# COMMAND ----------

# DBTITLE 1,copy annotation data to volume
# MAGIC %sh
# MAGIC cp -r /tmp/data/pcb1/image_anno.csv /Volumes/main__build/dbdemos_computer_vision_dl/pcb_training_data/labels/
