# Hexo Personal Blog Template

这是一个基于Hexo的个人博客模板，集成了GitHub Actions自动部署到GitHub Pages的功能。你可以使用这个模板快速搭建自己的个人博客网站。

## 特性

- 基于Hexo的静态博客系统
- GitHub Actions自动部署到GitHub Pages
- 支持Markdown格式写作
- 简洁的目录结构
- 完整的部署工作流配置

## 快速开始

1. 点击"Use this template"按钮创建你自己的仓库
2. 克隆你的仓库到本地：
   ```bash
   git clone https://github.com/你的用户名/你的仓库名.git
   cd 你的仓库名
   ```

3. 安装依赖：
   ```bash
   npm install
   ```

4. 本地预览：
   ```bash
   npm run server
   ```

5. 创建新文章：
   ```bash
   hexo new "文章标题"
   ```

## 部署说明

1. 在GitHub仓库设置中启用GitHub Pages，选择"GitHub Actions"作为构建和部署源。

2. 推送代码到main分支：
   ```bash
   git add .
   git commit -m "your commit message"
   git push origin main
   ```

3. GitHub Actions会自动构建并部署你的网站到GitHub Pages。

## 目录结构

```
.
├── _config.yml      # 网站配置文件
├── package.json     # 项目依赖配置
├── scaffolds/      # 模板文件夹
├── source/         # 源文件夹
│   ├── _posts/    # 文章文件夹
│   └── about/     # 关于页面
└── themes/        # 主题文件夹
```

## 自定义配置

1. 修改 `_config.yml` 文件来配置你的网站信息
2. 在 `source/_posts/` 目录下添加你的文章
3. 在 `themes/` 目录下可以安装和配置主题

## 注意事项

- 确保你的仓库已经启用了GitHub Pages
- 第一次部署可能需要等待几分钟
- 记得在 `_config.yml` 中设置正确的 `url` 和 `root` 值

## 许可证

MIT License