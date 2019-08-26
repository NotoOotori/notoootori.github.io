---
layout: default
title: Noto Ootori的学习笔记
---

<!-- markdownlint-disable MD025 -->
# {{ page.title }}
<!-- markdownlint-enable MD025 -->

{% for post in site.posts %}

  * * *

  <!-- markdownlint-disable MD023 -->
  ## [{{ post.title }}]({{ post.url | relative_url }})
  <!-- markdownlint-enable MD023 -->

  {{ post.excerpt }}

{% endfor %}
