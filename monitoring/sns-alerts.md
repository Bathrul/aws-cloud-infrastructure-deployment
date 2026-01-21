# SNS Alerts Configuration Guide

This document provides instructions for setting up Amazon SNS (Simple Notification Service) for alerts.

## Overview

Amazon SNS is a fully managed messaging service that enables you to send notifications from the cloud.

## Use Cases

- CloudWatch alarm notifications
- Application alerts
- System notifications
- Error notifications
- Auto Scaling notifications
- CloudFormation stack updates

## Setting Up SNS Topics

### Create SNS Topic

1. Navigate to SNS console
2. Click "Create topic"
3. Choose topic type:
   - **Standard**: Best-effort ordering, at-least-once delivery
   - **FIFO**: Strict ordering, exactly-once delivery
4. Enter topic name
5. Configure additional settings
6. Create topic

### Subscribe to Topic

1. Select the topic
2. Click "Create subscription"
3. Choose protocol:
   - Email
   - Email-JSON
   - SMS
   - HTTPS
   - Lambda
   - SQS
   - Application
4. Enter endpoint (email address, phone number, etc.)
5. Create subscription
6. Confirm subscription (for email/SMS)

## Integrating with CloudWatch

### Connecting Alarms to SNS

1. Create or edit CloudWatch alarm
2. In the "Actions" section
3. Select "Send a notification to"
4. Choose existing SNS topic or create new
5. Save alarm

### Example Alarm with SNS

```json
{
  "AlarmName": "HighCPUUtilization",
  "ComparisonOperator": "GreaterThanThreshold",
  "EvaluationPeriods": 2,
  "MetricName": "CPUUtilization",
  "Namespace": "AWS/EC2",
  "Period": 300,
  "Statistic": "Average",
  "Threshold": 80.0,
  "ActionsEnabled": true,
  "AlarmActions": [
    "arn:aws:sns:us-east-1:123456789012:MyTopic"
  ]
}
```

## Message Filtering

- Filter messages based on attributes
- Reduce noise by filtering at subscription level
- Use filter policies in JSON format

### Example Filter Policy

```json
{
  "severity": ["high", "critical"],
  "environment": ["production"]
}
```

## Access Control

### SNS Topic Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:us-east-1:123456789012:MyTopic"
    }
  ]
}
```

## Message Format

### Email Notification Example

```
Subject: ALARM: "HighCPUUtilization" in US East (N. Virginia)

You are receiving this email because your CloudWatch Alarm "HighCPUUtilization" 
in the US East (N. Virginia) region has entered the ALARM state.

Alarm Details:
- State Change: OK -> ALARM
- Reason: Threshold Crossed
- Timestamp: 2024-01-20 10:30:00 UTC
- Metric: CPUUtilization
- Current Value: 85%
- Threshold: 80%
```

## Testing SNS Topics

1. Select topic in SNS console
2. Click "Publish message"
3. Enter subject and message
4. Add message attributes (optional)
5. Publish
6. Verify delivery to subscribers

## Best Practices

- Use descriptive topic names
- Implement message filtering
- Set up subscription confirmation
- Use encryption for sensitive data
- Regular review of subscriptions
- Monitor SNS metrics in CloudWatch
- Use dead-letter queues for failed deliveries
- Implement proper access controls
- Tag topics for organization
- Document notification procedures
- Test alert delivery regularly
- Set up redundant notification channels
