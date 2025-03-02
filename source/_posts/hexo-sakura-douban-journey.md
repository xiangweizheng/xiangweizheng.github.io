---
title: 我的Hexo博客折腾记：Sakura主题与豆瓣插件的邂逅
date: 2024-03-01 15:51:00
tags: [技术, Hexo, 博客]
categories: 技术
---

## 缘起

最近一直想要搭建一个个人博客，记录生活和技术的点点滴滴。在浏览了众多Hexo主题后，被Sakura主题的清新优雅深深吸引，同时也想要通过豆瓣插件来展示我的阅读、观影历程。于是，今天决定开始这场说走就走的venture之旅。

## Node.js版本的纠葛

一开始信心满满地clone了Sakura主题，却在npm install时遇到了第一个坎。原来Sakura主题对Node.js版本有些挑剔，我的Node.js 22版本显得有点超前了。经过一番摸索，最后在package.json中明确指定了Node.js版本要求，这才解决了依赖安装的问题。

```json
{
  "engines": {
    "node": "22.0.4"
  }
}
```

## Sakura主题的个性化之旅

主题安装成功后，开始了令人期待的配置环节。修改_config.yml文件时，每一个选项都像是在为博客添加独特的个性：

- 设置了网站的基本信息
- 配置了令人心动的背景图片
- 调整了导航菜单的布局
- 添加了社交媒体链接

虽然过程中偶尔会遇到一些小问题，但看到配置生效后的效果，所有的努力都变得值得了。

## 豆瓣插件：记录生活的另一种方式

然后就到了配置豆瓣插件的环节。通过npm安装hexo-douban后，需要在配置文件中设置豆瓣账号信息。这个插件真的很棒，它可以自动同步我在豆瓣上的书评、影评，让博客内容更加丰富多彩。

特别让我兴奋的是，通过Python脚本可以自动获取豆瓣数据，这让内容的更新变得非常方便。虽然过程中遇到了一些API访问限制的问题，但通过适当的延时处理，最终也都完美解决了。

## 成果的喜悦

经过一天的venture，终于看到了令人满意的成果：
- 清新优雅的Sakura主题
- 完美运作的豆瓣同步功能
- 一个展现个性的个人空间

虽然这个过程中遇到了不少挑战，但每解决一个问题都会带来满满的成就感。这可能就是技术人的乐趣所在吧：在不断的探索和解决问题中，创造出属于自己的小天地。

## 后记

当然这是幻想的情况，实际是两个都没有成功。Sakura主题个性化配置不满意，先搁置了。在尝试运行 `hexo douban` 命令时遇到了以下错误，尝试了多个node版本(20,18,16,12)也还是一样的问题：

```bash
PS F:\oneapponemonth\hexo_personal_page> hexo douban
```
(node:45692) ExperimentalWarning: The fs.promises API is experimental
INFO  Validating config
FATAL 
TypeError: Object.fromEntries is not a function
    at then.filter.then.modules (F:\oneapponemonth\hexo_personal_page\node_modules\hexo\dist\hexo\load_plugins.js:36:23)        
    at tryCatcher (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\util.js:16:23)
    at Promise._settlePromiseFromHandler (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:547:31)
    at Promise._settlePromise (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:604:18)
    at Promise._settlePromise0 (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:649:10)        
    at Promise._settlePromises (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:729:18)        
    at Promise._fulfill (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:673:18)
    at MappingPromiseArray.PromiseArray._resolve (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise_array.js:127:19)
    at MappingPromiseArray._filter (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\map.js:134:10)        
    at MappingPromiseArray._promiseFulfilled (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\map.js:106:18)
    at Promise._settlePromise (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:609:26)
    at Promise._settlePromise0 (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:649:10)        
    at Promise._settlePromises (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\promise.js:729:18)        
    at _drainQueueStep (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\async.js:93:12)
    at _drainQueue (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\async.js:86:9)
    at Async._drainQueues (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\async.js:102:5)
    at Immediate.Async.drainQueues [as _onImmediate] (F:\oneapponemonth\hexo_personal_page\node_modules\bluebird\js\release\async.js:15:14)
    at processImmediate (internal/timers.js:443:21)