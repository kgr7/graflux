import os
import time
import random
from influxdb_client import InfluxDBClient, Point, BucketsApi
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = os.environ["INFLUX_BUCKET"]
token = os.environ["INFLUX_TOKEN"]
url = os.environ["INFLUX_URL"]
org = os.environ["INFLUX_ORG"]

client = InfluxDBClient(url="http://influxdb:8086", token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)

for i in range(10000):
  p = Point("random_measurement").tag("data", "Value").field("value", random.uniform(16, 24))
  write_api.write(bucket=bucket, record=p)
  time.sleep(0.1)
