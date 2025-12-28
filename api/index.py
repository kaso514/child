# Vercel Serverless函数入口 - 简化版本

import os
import sys

# 添加项目路径到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# 设置Django环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datetime_project.settings')

# 导入Django WSGI应用
from datetime_project.wsgi import application

# 简单的请求处理函数
def handler(request):
    """
    处理HTTP请求
    """
    # 导入必要的模块
    from io import BytesIO
    import json
    
    # 解析请求
    method = request.get('method', 'GET')
    path = request.get('path', '/')
    headers = request.get('headers', {})
    body = request.get('body', '')
    
    # 创建WSGI环境
    environ = {
        'REQUEST_METHOD': method,
        'SCRIPT_NAME': '',
        'PATH_INFO': path,
        'QUERY_STRING': request.get('query', ''),
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': '80',
        'HTTP_HOST': headers.get('host', 'localhost'),
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https' if headers.get('x-forwarded-proto') == 'https' else 'http',
        'wsgi.input': BytesIO(body.encode() if body else b''),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    
    # 添加HTTP头信息
    for key, value in headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value
    
    # 调用Django应用
    def start_response(status, response_headers, exc_info=None):
        nonlocal response_status, response_headers_list
        response_status = status
        response_headers_list = response_headers
    
    response_status = None
    response_headers_list = []
    response_body = []
    
    result = application(environ, start_response)
    
    # 收集响应体
    for data in result:
        response_body.append(data)
    
    # 构建响应
    return {
        'statusCode': int(response_status.split(' ')[0]) if response_status else 200,
        'headers': dict(response_headers_list),
        'body': b''.join(response_body).decode('utf-8')
    }

# Vercel函数入口
def app(request, context):
    """
    Vercel Serverless函数处理程序
    """
    return handler(request)