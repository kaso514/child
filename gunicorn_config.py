# Gunicorn配置文件
# 用于生产环境部署

bind = "0.0.0.0:8000"
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
max_requests = 1000
max_requests_jitter = 100
preload_app = True