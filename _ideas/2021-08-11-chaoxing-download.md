---
tags: 超星学习通 直链下载
---
<!-- markdownlint-disable MD041 -->
参考[回答](https://www.zhihu.com/question/320181398/answer/1039330532), 可以利用如下方法直链下载超星学习通中的课件. 通过浏览器打开超星学习通, 进入 F12 界面的 DOM 资源管理器. 通过查找可以找到课件的 "object_id", 而
> http<nolink>://d0.ananas.chaoxing.com/download/&lt;objectid&gt;
即为我们要找的下载链接.

注: 这里我们通过添加一个无意义的 HTML 空元素 `<nolink>` 来避免 URL 被添加超链接, 参考自这个[回答](https://meta.stackexchange.com/a/119811).
