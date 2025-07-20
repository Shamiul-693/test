async def app(scope, receive, send):
    if scope['type'] == 'http':
        response_body = b"this is my uvicorn webserver learning"
        headers = [(b'content-type', b'text/plain')]
        
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': headers,
        })
        
        await send({
            'type': 'http.response.body',
            'body': response_body,
        })
    else:
        raise NotImplementedError("Only HTTP scope is supported")