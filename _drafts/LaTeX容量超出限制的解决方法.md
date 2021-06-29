---
title: LaTeX容量超出限制的解决方法
tags: LaTeX, MikTeX
description: TeX capacity exceeded.
---

## 添加容量

```bash
    initexmf --edit-config-file=xelatex
```

```plaintext
    main_memory = 90000000
```

```bash
    initexmf --dump=xelatex
```

## 参考资料

1. <https://tex.stackexchange.com/a/548335/>
