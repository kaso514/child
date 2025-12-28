# Vercel Serverless函数入口
# 专门为Django应用优化的Vercel部署方案

import os
import sys

# 添加项目路径到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# 设置Django环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datetime_project.settings')

# 导入Django WSGI应用
from datetime_project.wsgi import application

# 使用mangum适配器将WSGI应用转换为ASGI应用
from mangum import Mangum

# 创建Mangum适配器
handler = Mangum(application, lifespan="off")

def lambda_handler(event, context):
    """
    AWS Lambda兼容的处理函数
    """
    return handler(event, context)