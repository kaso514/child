# Heroku 部署指南 - 推荐方案

## 为什么选择Heroku而不是Vercel？

- ✅ **专门为Python应用设计** - Heroku对Django支持非常好
- ✅ **部署简单** - 一键部署，无需复杂配置
- ✅ **免费额度** - 每月有550小时的免费使用时间
- ✅ **成熟稳定** - 多年的Python应用部署经验
- ✅ **错误诊断简单** - 日志查看方便

## 部署步骤

### 第一步：准备代码

确保你的代码已经推送到GitHub：

```bash
git add .
git commit -m "添加Heroku部署配置"
git push origin main
```

### 第二步：创建Heroku应用

1. **注册Heroku账号**
   - 访问 [heroku.com](https://heroku.com)
   - 注册免费账号

2. **安装Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # 或者下载安装包
   # 访问 https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **登录Heroku**
   ```bash
   heroku login
   ```

4. **创建Heroku应用**
   ```bash
   heroku create your-app-name
   ```
   
   *注意：应用名需要唯一，比如：`datetime-display-123`*

### 第三步：设置环境变量

```bash
# 设置Django密钥
heroku config:set SECRET_KEY=你的安全密钥

# 关闭调试模式
heroku config:set DEBUG=False

# 设置时区
heroku config:set TZ=Asia/Shanghai
```

### 第四步：部署应用

```bash
# 部署到Heroku
git push heroku main

# 运行数据库迁移
heroku run python manage.py migrate

# 收集静态文件
heroku run python manage.py collectstatic --noinput
```

### 第五步：打开应用

```bash
heroku open
```

## 配置文件说明

### Procfile
```
web: gunicorn datetime_project.wsgi --bind 0.0.0.0:$PORT
```
- 告诉Heroku如何启动你的Django应用
- 使用Gunicorn作为WSGI服务器

### requirements.txt
已包含所有必要的依赖：
- Django 4.2.7
- Gunicorn (WSGI服务器)
- Whitenoise (静态文件服务)

## 环境变量设置

在Heroku控制台设置以下环境变量：

| 变量名 | 值 | 说明 |
|--------|----|------|
| `SECRET_KEY` | 安全密钥 | Django安全密钥 |
| `DEBUG` | `False` | 生产环境关闭调试 |
| `TZ` | `Asia/Shanghai` | 设置时区 |

### 生成SECRET_KEY
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

## 验证部署

部署完成后，访问你的Heroku应用URL（如：`https://your-app-name.herokuapp.com`），应该能看到日期时间显示页面。

## 查看日志

如果遇到问题，可以查看Heroku日志：

```bash
# 查看实时日志
heroku logs --tail

# 查看最近日志
heroku logs
```

## 常见问题解决

### 1. 应用无法启动
- 检查Procfile格式是否正确
- 确认requirements.txt包含所有依赖
- 查看Heroku日志定位问题

### 2. 静态文件404
- 确保运行了`collectstatic`命令
- 检查Whitenoise配置

### 3. 数据库错误
- 确保运行了数据库迁移
- Heroku使用PostgreSQL，但SQLite在免费层也可用

## 优势对比

| 特性 | Heroku | Vercel |
|------|--------|--------|
| Python支持 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Django支持 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 部署难度 | ⭐⭐ | ⭐⭐⭐⭐ |
| 免费额度 | 550小时/月 | 有限 |
| 稳定性 | 高 | 中等 |

## 后续维护

### 更新应用
```bash
git add .
git commit -m "更新描述"
git push heroku main
```

### 缩放应用
```bash
# 查看当前状态
heroku ps

# 重启应用
heroku restart
```

---

**强烈推荐使用Heroku部署Django项目**，它会比Vercel稳定得多，而且部署过程更加顺畅！