# CloudTrail Configuration Guide

This document provides instructions for setting up AWS CloudTrail for auditing and compliance.

## Overview

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account.

## What CloudTrail Records

- API calls made in your AWS account
- User identity
- Time of API call
- Source IP address
- Request parameters
- Response elements
- Console sign-in events

## Setting Up CloudTrail

### Create a Trail

1. Navigate to CloudTrail console
2. Click "Create trail"
3. Configure trail settings:
   - **Trail name**: Descriptive name
   - **Storage location**: S3 bucket
   - **Log file SSE-KMS encryption**: Recommended
   - **Log file validation**: Enable for integrity
   - **SNS notification**: Optional
   - **CloudWatch Logs**: Optional integration

4. Choose events to log:
   - **Management events**: Control plane operations
   - **Data events**: S3 object-level operations, Lambda function executions
   - **Insights events**: Detect unusual activity

5. Review and create

### Multi-Region Trail

- Recommended for comprehensive auditing
- Captures events from all regions
- Single S3 bucket for all events

### Organization Trail

- For AWS Organizations
- Captures events across all accounts
- Centralized logging and monitoring

## CloudTrail Integration

### With CloudWatch Logs

1. Enable CloudWatch Logs integration
2. Create IAM role for CloudTrail
3. Specify log group
4. Set up metric filters
5. Create alarms for security events

### Example Metric Filters

**Unauthorized API Calls**
```
{ ($.errorCode = "*UnauthorizedOperation") || ($.errorCode = "AccessDenied*") }
```

**Root Account Usage**
```
{ $.userIdentity.type = "Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != "AwsServiceEvent" }
```

**Security Group Changes**
```
{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) }
```

## Analyzing CloudTrail Logs

### Using AWS Athena

1. Create Athena table from CloudTrail logs
2. Run SQL queries for analysis
3. Identify patterns and anomalies

### Example Athena Query

```sql
SELECT
  useridentity.principalid,
  eventname,
  sourceipaddress,
  eventtime
FROM cloudtrail_logs
WHERE eventtime > '2024-01-01'
  AND errorcode IS NOT NULL
ORDER BY eventtime DESC
LIMIT 100;
```

### Using CloudTrail Event History

- View recent events (90 days)
- Filter by user, resource, event name
- Quick lookup for troubleshooting

## Security Best Practices

### S3 Bucket Security

- Enable bucket versioning
- Configure bucket lifecycle policies
- Enable MFA Delete
- Block public access
- Enable server access logging

### Encryption

- Use SSE-KMS encryption
- Manage KMS keys properly
- Regular key rotation

### Access Control

- Restrict S3 bucket access
- Use least privilege IAM policies
- Enable log file validation
- Separate logging account

### Monitoring

- Set up CloudWatch alarms
- Monitor for suspicious activity
- Regular log review
- Automate security responses

## Compliance Use Cases

- **PCI DSS**: Track and monitor access to cardholder data
- **HIPAA**: Audit access to protected health information
- **SOC 2**: Demonstrate security controls
- **GDPR**: Track data access and changes

## Log File Format

CloudTrail log files are in JSON format:

```json
{
  "Records": [
    {
      "eventVersion": "1.08",
      "userIdentity": {...},
      "eventTime": "2024-01-20T10:00:00Z",
      "eventSource": "ec2.amazonaws.com",
      "eventName": "RunInstances",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.1",
      "userAgent": "aws-cli/2.0.0",
      "requestParameters": {...},
      "responseElements": {...}
    }
  ]
}
```

## Cost Optimization

- First copy of management events is free
- Data events and additional copies incur charges
- Use S3 lifecycle policies to archive old logs
- Consider log file aggregation

## Best Practices

- Enable CloudTrail in all regions
- Use organization trails
- Enable log file validation
- Encrypt log files
- Regular log review and analysis
- Set up automated alerting
- Integrate with SIEM solutions
- Document incident response procedures
- Protect CloudTrail configuration
- Monitor CloudTrail itself
- Regular compliance audits
