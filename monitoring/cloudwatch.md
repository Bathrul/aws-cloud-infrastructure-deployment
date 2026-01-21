# CloudWatch Monitoring Guide

This document provides instructions for setting up Amazon CloudWatch monitoring.

## Overview

Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights for AWS resources and applications.

## CloudWatch Components

### Metrics
- **Built-in Metrics**: Automatically collected from AWS services
- **Custom Metrics**: Application-specific metrics
- **Metric Math**: Perform calculations on metrics

### Logs
- **Log Groups**: Organize logs by application/service
- **Log Streams**: Individual log sequences
- **Log Insights**: Query and analyze log data

### Alarms
- **Metric Alarms**: Trigger based on metric thresholds
- **Composite Alarms**: Combine multiple alarms
- **Actions**: SNS notifications, Auto Scaling, EC2 actions

### Dashboards
- Visualize metrics
- Create custom views
- Share with team members

## Setting Up CloudWatch

### For EC2 Instances

1. **Install CloudWatch Agent**
   ```bash
   wget https://s3.amazonaws.com/amazoncloudwatch-agent/linux/amd64/latest/AmazonCloudWatchAgent.zip
   unzip AmazonCloudWatchAgent.zip
   sudo ./install.sh
   ```

2. **Configure Agent**
   - Create configuration file
   - Specify metrics to collect
   - Configure log collection

3. **Start Agent**
   ```bash
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
     -a fetch-config \
     -m ec2 \
     -s \
     -c file:/opt/aws/amazon-cloudwatch-agent/etc/config.json
   ```

### For Lambda Functions

- Automatically integrated
- Logs sent to CloudWatch Logs
- Metrics available in CloudWatch

### For RDS

- Enable Enhanced Monitoring
- View metrics in CloudWatch console
- Set up alarms for key metrics

## Key Metrics to Monitor

### EC2
- CPUUtilization
- NetworkIn/NetworkOut
- DiskReadOps/DiskWriteOps
- StatusCheckFailed

### RDS
- CPUUtilization
- DatabaseConnections
- FreeableMemory
- ReadLatency/WriteLatency

### Lambda
- Invocations
- Duration
- Errors
- Throttles

### S3
- BucketSizeBytes
- NumberOfObjects
- AllRequests
- 4xxErrors/5xxErrors

## Creating Alarms

1. Navigate to CloudWatch console
2. Select "Alarms" → "Create alarm"
3. Choose metric
4. Define conditions
5. Configure actions (SNS topic)
6. Set alarm name and description
7. Review and create

## Best Practices

- Set up alarms for critical metrics
- Use composite alarms for complex scenarios
- Create dashboards for quick overview
- Enable detailed monitoring for EC2
- Use metric filters for log-based metrics
- Set appropriate alarm thresholds
- Use anomaly detection
- Regular review of metrics and alarms
- Tag resources for better organization
