# Youtube-Data-Analysis-Data-engineering-Project
In this project, we will execute the END TO END DATA ENGINEERING PROJECT using Kaggle YouTube Trending Dataset. 

# Overview
This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

# Data Architecture Diagram
![Screenshot 2024-05-15 153007](https://github.com/ayuvgr8/youtube-data-analysis-data-engineering-project/assets/49532650/55fa2fbe-98f5-4d76-b229-175a3a636f7c)


# Project Goals :
1. Data Ingestion — Build a mechanism to ingest data from different sources
2. ETL System — We are getting data in raw format, transforming this data into the proper format
3. Data lake — We will be getting data from multiple sources so we need centralized repo to store them
4. Scalability — As the size of our data increases, we need to make sure our system scales with it
5. Cloud — We can’t process vast amounts of data on our local computer so we need to use the cloud, in this case, we will use AWS
6. Reporting — Build a dashboard to get answers to the question we asked earlier

# Major Task Execution :
>> Developed a robust data ingestion system using AWS services to efficiently collect and manage data from multiple sources, ensuring high data availability and security.

>> Implemented an ETL pipeline using AWS Glue to transform raw data into structured formats, facilitating seamless integration and analysis.

>> Designed and maintained a centralized data lake on Amazon S3, providing scalable storage solutions for diverse datasets and ensuring easy access for analytical processing.

>> Leveraged AWS Lambda and AWS Athena for scalable, serverless data processing and interactive querying, enhancing system performance and reducing operational costs.

>>Created dynamic dashboards with Amazon QuickSight, delivering real-time insights and comprehensive reports to support data-driven decision-making.

# AWS Services Used :
1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
2. AWS IAM: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
3. QuickSight: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
5. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.
6. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.


# Dataset Used :
This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.
https://www.kaggle.com/datasets/datasnaek/youtube-new


# Note :

This is for those who facing issues while updated Features of AWS-
1) Replace awswrangler with awssdkpandas in the code. The rest code remains the same.
2) Add Layer : AWSDataWrangler-Python3.8 replaced it with AWSSDKPandas-Python3.8 version 10
3) Create db_youtube_cleaned db using Glue or Athena before running the code.
4) For Task timed out issue - increasing the memory along with time, for eg. time = 5 min, memory = 512 MB 
5) To anyone facing issues with Glue job for CSV file to Parquet conversion (As ETL Legacy has been discontinued), follow the below steps -

      Create a Visual Glue ETL job using Source - AWS Glue Data Catalog >> Transform - Change Schema >> Target - S3 (You can add partition key as 'region' in here now, rather than adding it later in the script). Then add 
      predicate_pushdown as mentioned in the video and you're good to go.

