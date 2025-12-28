# Vercel 部署指南

## 问题分析

你遇到的404错误是因为Vercel默认是为静态网站设计的，而Django是一个动态的Python Web框架。需要特殊的Serverless函数配置才能正确部署。

## 已完成的配置

我已经为你创建了以下Vercel部署所需的文件：

1. **`vercel.json`** - Vercel配置文件
2. **`api/index.py`** - Serverless函数入口
3. **更新的`requirements.txt`** - 添加了mangum适配器
4. **更新的`settings.py`** - 适配生产环境设置
5. **`.env.example`** - 环境变量配置示例

## 部署步骤

### 第一步：推送代码到GitHub

```bash
git add .
git commit -m "添加Vercel部署配置"
git push origin main
```

### 第二步：在Vercel中部署

1. **登录Vercel**
   - 访问 [vercel.com](https://vercel.com)
   - 使用GitHub账号登录

2. **导入项目**
   - 点击 "New Project"
   - 选择你的GitHub仓库
   - 选择 "Import"

3. **配置环境变量**
   - 在项目设置中，找到 "Environment Variables"
   - 添加以下环境变量：
     ```
     SECRET_KEY=your-very-secure-secret-key-here
     DEBUG=False
     TZ=Asia/Shanghai
     ```

4. **开始部署**
   - 点击 "Deploy"
   - Vercel会自动检测配置并部署

### 第三步：验证部署

部署完成后，访问Vercel提供的域名，应该能看到日期时间显示页面。

## 配置说明

### Vercel配置文件 (`vercel.json`)

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

### Serverless函数 (`api/index.py`)

使用mangum库将Django的WSGI应用转换为Vercel兼容的Serverless函数。

## 常见问题解决

### 1. 404错误
- 确保`vercel.json`配置正确
- 检查路由配置
- 验证Serverless函数是否正常启动

### 2. 500错误
- 检查环境变量配置
- 查看Vercel部署日志
- 确认依赖包安装正确

### 3. 静态文件问题
- Django的静态文件在Serverless环境中需要特殊处理
- 可以考虑使用CDN服务

## 生产环境建议

1. **安全设置**
   - 使用强密码生成SECRET_KEY
   - 设置DEBUG=False
   - 配置合适的ALLOWED_HOSTS

2. **性能优化**
   - 考虑使用数据库连接池
   - 启用缓存机制
   - 优化静态文件服务

3. **监控和日志**
   - 配置错误监控
   - 设置日志记录
   - 使用性能监控工具

## 替代方案

如果Vercel部署仍有问题，可以考虑以下替代方案：

1. **Heroku** - 对Python应用支持更好
2. **Railway** - 现代化的部署平台
3. **PythonAnywhere** - 专门为Python设计
4. **DigitalOcean App Platform** - 灵活的部署选项

## 技术支持

如果部署过程中遇到问题，可以：

1. 查看Vercel的部署日志
2. 检查环境变量配置
3. 验证代码是否已正确推送
4. 参考Django官方部署文档

---

**注意**: 首次部署可能需要一些时间，Vercel需要安装所有依赖包并构建应用。