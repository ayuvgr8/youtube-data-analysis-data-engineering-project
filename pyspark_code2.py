import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1716066030169 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://de-on-youtube-analysis-raw-apsouth1-dev"], "recurse": True}, transformation_ctx="AmazonS3_node1716066030169")

# Script generated for node Change Schema
ChangeSchema_node1716066376094 = ApplyMapping.apply(frame=AmazonS3_node1716066030169, mappings=[("video_id", "string", "video_id", "string"), ("trending_date", "string", "trending_date", "string"), ("title", "string", "title", "string"), ("channel_title", "string", "channel_title", "string"), ("category_id", "string", "category_id", "bigint"), ("publish_time", "string", "publish_time", "string"), ("tags", "string", "tags", "string"), ("views", "string", "views", "string"), ("likes", "string", "likes", "bigint"), ("dislikes", "string", "dislikes", "bigint"), ("comment_count", "string", "comment_count", "bigint"), ("thumbnail_link", "string", "thumbnail_link", "string"), ("comments_disabled", "string", "comments_disabled", "boolean"), ("ratings_disabled", "string", "ratings_disabled", "boolean"), ("video_error_or_removed", "string", "video_error_or_removed", "boolean"), ("description", "string", "description", "string")], transformation_ctx="ChangeSchema_node1716066376094")

# Script generated for node Amazon S3
AmazonS3_node1716066484947 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1716066376094, connection_type="s3", format="glueparquet", connection_options={"path": "s3://de-on-youtube-analysis-cleansed-apsouth1-dev/youtube/raw_statistics/", "partitionKeys": ["region"]}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1716066484947")

job.commit()
