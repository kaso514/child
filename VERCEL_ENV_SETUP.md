# Vercel 环境变量设置指南

## SECRET_KEY 设置步骤

### 第一步：生成安全的SECRET_KEY

在终端中运行以下命令生成密钥：

```bash
# 方法1：使用Python secrets模块
python3 -c "import secrets; print(secrets.token_urlsafe(50))"

# 方法2：使用Django内置函数
python3 manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

复制生成的密钥字符串。

### 第二步：在Vercel中设置环境变量

1. **登录Vercel**
   - 访问 https://vercel.com
   - 使用GitHub账号登录

2. **选择项目**
   - 在Dashboard中找到你的项目
   - 点击项目名称进入详情页

3. **进入设置**
   - 点击顶部的 **Settings** 标签
   - 在左侧菜单选择 **Environment Variables**

4. **添加环境变量**
   - 点击 **Add New** 按钮
   - 分别添加以下变量：

   | 变量名 | 值 | 说明 |
   |--------|----|------|
   | `SECRET_KEY` | 你生成的密钥 | Django安全密钥 |
   | `DEBUG` | `False` | 生产环境关闭调试 |
   | `TZ` | `Asia/Shanghai` | 设置时区 |

5. **保存并重新部署**
   - 点击 **Save** 保存设置
   - 返回项目页面，点击 **Redeploy** 重新部署

### 第三步：验证设置

部署完成后，访问你的Vercel域名，应该能看到日期时间显示页面正常工作。

## 环境变量说明

### SECRET_KEY
- **作用**: Django的安全密钥，用于加密会话、密码重置等
- **要求**: 必须足够长且随机，不能泄露
- **示例**: `django-insecure-your-very-long-random-string-here`

### DEBUG
- **作用**: 控制调试模式
- **生产环境**: 必须设置为 `False`
- **开发环境**: 可以设置为 `True`

### TZ
- **作用**: 设置服务器时区
- **推荐值**: `Asia/Shanghai` (中国时区)

## 常见问题

### Q: 如果忘记设置SECRET_KEY会怎样？
A: Django会使用settings.py中的默认值，但在生产环境这是不安全的。

### Q: 如何知道环境变量是否生效？
A: 可以在Vercel的部署日志中查看，或者添加一个测试页面显示环境变量。

### Q: 可以设置多个环境吗？
A: 可以，Vercel支持Production、Preview、Development不同环境的环境变量。

## 安全建议

1. **不要将SECRET_KEY提交到GitHub**
2. **定期更换SECRET_KEY**
3. **使用不同的密钥用于不同环境**
4. **确保DEBUG在生产环境为False**

## 替代方案

如果Vercel环境变量设置复杂，也可以考虑：

1. **使用.env文件**（但需要确保不提交到GitHub）
2. **使用其他部署平台**如Heroku，它们的环境变量设置更直观
3. **使用密钥管理服务**如AWS Secrets Manager

---

**重要提醒**: 设置完环境变量后，必须重新部署项目才能生效！