---
title: Jekyll 静态博客搭建
tags: Jekyll 静态博客
description: Jekyll 是 Github Page 默认的静态博客引擎, 优点在于用户可以对最终的网页有比较完整的把握. 这篇文章旨在简要介绍使用 Jekyll 搭建静态博客中需要注意的事项.
---

## 安装

<https://jekyllrb.com/docs/installation/>

## 在本地运行

自动重新生成网页.

```shell
bundle exec jekyll serve --force-polling
```

<https://theta360developers.github.io/webapi/tester/2021/02/07/jekyll-on-wsl2.html>

## 撰写博客

使用 Kramdown 引擎, 取消了 Kramdown 的代码块高亮, 而是使用 highlight.js.

## 部署网站

<https://github.com/helaili/jekyll-action>
