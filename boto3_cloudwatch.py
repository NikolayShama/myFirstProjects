#!/usr/bin/python
import boto3, sys
import datetime

#Connection_ID = sys.argv[1]
#MetricName = sys.argv[2]
Connection_ID = <...>
MetricName = <...>

cw = boto3.client(
            'cloudwatch',
            aws_access_key_id= <...>,
            aws_secret_access_key= <...>
            )

response = cw.get_metric_statistics(
            Period=60,
            StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=60),
            EndTime=datetime.datetime.utcnow(),
            MetricName=MetricName,
            Namespace='AWS/DX',
            Statistics=['Average'],
            Dimensions=[{'Name':'ConnectionId', 'Value':Connection_ID}]
            )
print(response['Datapoints'][0]['Average'])


"""

response = cw.get_metric_statistics(
            Period=300,
            StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
            EndTime=datetime.datetime.utcnow(),
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Statistics=['Average'],
            Dimensions=[{'Name':'InstanceId', 'Value':'i-04fe50529ae44b23a'}]
            )
print(response['Datapoints'][0]['Average'])

"""