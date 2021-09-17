import os
import time
import random
from datetime import datetime
from influxdb import InfluxDBClient

user = os.environ["INFLUX_USER"]
password = os.environ["INFLUX_PASS"]

client = InfluxDBClient('influxdb', 8086, user, password, 'example')
client.create_database('example')

while True:    
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server_01",
                "region": "us_west"
            },
            "time": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fields": {
                "value": random.uniform(0, 1)
            }
        }
    ]

    client.write_points(json_body)
    result = client.query('select value from cpu_load_short;')
    print("Result: {0}".format(result))
    time.sleep(1)

