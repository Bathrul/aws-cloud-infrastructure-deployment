"""
AWS Lambda Function Example

This is a sample Lambda function that demonstrates basic functionality.
Modify this template based on your specific use case.
"""

import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Main Lambda handler function
    
    Args:
        event: Event data passed to the function
        context: Runtime information
    
    Returns:
        dict: Response object with statusCode and body
    """
    
    # Log the incoming event
    logger.info(f"Received event: {json.dumps(event)}")
    
    try:
        # Extract data from event
        # Modify this based on your event source (API Gateway, S3, SNS, etc.)
        
        # Example: Process the event
        result = process_event(event)
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Success',
                'result': result
            })
        }
        
    except Exception as e:
        # Log error
        logger.error(f"Error processing event: {str(e)}", exc_info=True)
        
        # Return error response
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Internal server error',
                'error': str(e)
            })
        }


def process_event(event):
    """
    Process the event data
    
    Args:
        event: Event data to process
    
    Returns:
        dict: Processed result
    """
    
    # Add your business logic here
    # This is a placeholder implementation
    
    return {
        'processed': True,
        'timestamp': context.get_remaining_time_in_millis() if 'context' in globals() else 0
    }


# Additional helper functions can be added below
