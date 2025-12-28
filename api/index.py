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

# Vercel函数入口 - 直接返回Django应用
# Vercel会自动检测并调用这个函数
def app(event, context):
    """
    Vercel Serverless函数处理程序
    """
    # 导入Mangum适配器
    from mangum import Mangum
    
    # 创建Mangum适配器实例
    handler = Mangum(application, lifespan="off")
    
    # 返回处理结果
    return handler(event, context)