---
layout: default
title: Study Notes
---

<!-- markdownlint-disable MD025 -->
# Study Notes
<!-- markdownlint-enable MD025 -->

{% for post in site.posts %}

  * * *

  <!-- markdownlint-disable MD023 -->
  ## [{{ post.title }}]({{ post.url | relative_url }})
  <!-- markdownlint-enable MD023 -->

  {{ post.excerpt }}

{% endfor %}
