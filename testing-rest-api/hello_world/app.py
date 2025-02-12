import json

employees = [
    {
        'name': 'bob',
        'employee_id': 121
    }
]
def lambda_handler(event, context):

    result = ''
    if event['httpMethod'] ==  "GET" and event['resource'] == '/employee':
        result = json.dumps(employees)
    elif (event['httpMethod'] == "POST") and (event['resource'] == '/employee'):
        employees.append(json.loads(event['body']))
        result = json.dumps(employees)
    
    response = {
        'statusCode': 200,
        'body': json.dumps({
                'message': result
               })
    }
    return response
    
    
    
