import boto3
import os
import sys
import botocore
import pandas as pd
from pyspark.sql import SparkSession
# import s3fs

class main():

    global inputFilePath,bucketName,s3Key
    inputFilePath  = 'C:/Users/gangutsy/Desktop/git testing/test111.csv'
    bucketName     = 'newfg'
    s3Key          = 'test111.csv'

    def __init__(self):
        pass

    def readFile(self):
        pass

    def createObjBucket(self):
        print('testing starts')
        s3  =  boto3.resource('s3')
        # Check if the buckcet and object already exist
        try:
            print('testing starts1')
            buckResponse = s3.meta.client.head_bucket(Bucket=bucketName)
            if buckResponse:
                    print('Bucket already exist can not be created again')

        except Exception as e:
            pass
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print(e.response['Error'])
        except 'objNotFound':
            pass

        self.createObj(s3)

        return True

    def createObj(self,s3):
        try:
            objResponse = s3.meta.client.head_object(Bucket=bucketName, Key=s3Key)

            if objResponse:
                    # delete object first
                    self.deleteObj(s3)


        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print(f"object {s3Key} not found and creating the object")
                response = s3.meta.client.upload_file(inputFilePath, bucketName,s3Key)
        return True

    def deleteObj(self,s3):
        response = s3.meta. client.delete_object(
                        Bucket=bucketName,
                        Key=s3Key)
        if response:
            print(f'object {s3Key} got deleted in {bucketName} bucket')
        self.createObj(s3)
        return True 

    # def readCsvFile(self):
    #     df = spark.read.csv(inputFilePath,header=True)
    #     df = df.toPandas()
    #     bytes_to_write = df.to_csv(None).encode()
    #     fs = s3fs.S3FileSystem(key=xxxxxxxxxx, secret=xxxxxxxxxxxx)
    #     with fs.open('s3://bucketName/file.csv', 'wb') as f:
    #         f.write(bytes_to_write)


if __name__ == "__main__":
    print('in main method to run the proj')
    spark = SparkSession \
            .builder \
            .appName("Python Spark").getOrCreate()
    obj1 = main()
    obj1.read
    obj1.createObjBucket()
