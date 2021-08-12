---
tags: Git
---
<!-- markdownlint-disable MD041 -->
参考[博客](https://www.internalpointers.com/post/squash-commits-into-one-git), 我们可以通过 `git-rebase --interactive [<upstream> [<branch>]]` 来合并一些 commit, 这有助于在 push 之前整理好 commit tree. 其中 `<upstream>` 指的是想合并的那些 commit 之前的一个 commit, 然后使用过程中注意要 pick 第一个 commit, 然后 squash 你想合并的 commit, 具体可以看命令行中会出现的注释说明.
