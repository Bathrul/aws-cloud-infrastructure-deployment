# RDS Setup Guide

This document provides instructions for setting up Amazon RDS (Relational Database Service).

## Prerequisites

- AWS Account
- VPC with at least two subnets in different AZs
- Security groups configured
- Database subnet group

## Database Engine Selection

- Amazon Aurora (MySQL/PostgreSQL compatible)
- MySQL
- PostgreSQL
- MariaDB
- Oracle
- SQL Server

## RDS Instance Configuration

### Instance Specifications

- **DB Instance Class**: Choose based on workload (db.t3.micro, db.m5.large, etc.)
- **Storage Type**: General Purpose (SSD), Provisioned IOPS (SSD)
- **Allocated Storage**: Initial storage size
- **Storage Autoscaling**: Enable for automatic growth

### High Availability

- **Multi-AZ Deployment**: For production workloads
- **Read Replicas**: For read-heavy workloads
- **Backup Retention**: 7-35 days

### Security

- **VPC**: Deploy in private subnet
- **Security Groups**: Control network access
- **Encryption**: At rest and in transit
- **IAM Database Authentication**: For enhanced security

## Setup Steps

1. Navigate to RDS console
2. Click "Create database"
3. Choose creation method (Standard/Easy create)
4. Select engine type and version
5. Choose template (Production, Dev/Test, Free tier)
6. Configure settings
   - DB instance identifier
   - Master username and password
7. Configure instance size
8. Configure storage
9. Configure connectivity
   - VPC and subnet group
   - Public access (No for production)
   - Security group
10. Configure additional settings
    - Backup
    - Monitoring
    - Maintenance window
11. Review and create

## Post-Creation Configuration

- Create database users
- Configure parameter groups
- Set up monitoring alarms
- Test connectivity
- Configure automated backups
- Set up CloudWatch alarms

## Best Practices

- Use Multi-AZ for production
- Enable automated backups
- Use encryption at rest
- Use SSL/TLS for connections
- Regular snapshots
- Monitor performance metrics
- Use parameter groups for configuration
- Implement least privilege access
- Regular security patches
