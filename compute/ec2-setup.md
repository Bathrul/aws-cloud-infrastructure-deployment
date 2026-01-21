# EC2 Setup Guide

This document provides instructions for setting up Amazon EC2 instances.

## Prerequisites

- AWS Account
- VPC and subnets configured
- Security groups created
- Key pair for SSH access

## EC2 Instance Configuration

### Instance Type
- Choose appropriate instance type based on workload
- Example: t2.micro for testing, t3.medium for production

### AMI Selection
- Amazon Linux 2
- Ubuntu Server
- Windows Server

### Storage
- EBS volumes
- Instance store (ephemeral)

### Security Groups
- Configure inbound/outbound rules
- Limit access to specific IP ranges
- Use least privilege principle

## Launch Steps

1. Navigate to EC2 console
2. Click "Launch Instance"
3. Select AMI
4. Choose instance type
5. Configure instance details
6. Add storage
7. Add tags
8. Configure security group
9. Review and launch
10. Select key pair

## Post-Launch Configuration

- Connect to instance via SSH/RDP
- Install required software
- Configure application
- Set up monitoring
- Create AMI for backup

## Best Practices

- Use Auto Scaling groups
- Enable detailed monitoring
- Regular patching and updates
- Use IAM roles instead of access keys
- Enable encryption for EBS volumes
