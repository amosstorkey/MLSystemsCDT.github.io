---
layout: page
permalink: /gpu_resources/
redirect_from:
  - /gpu_resources
  - /gpu_resources.html
title: GPU Resources
---

For more information about accessible **GPU clusters**, see the informatics
documentation:
<http://computing.help.inf.ed.ac.uk/cluster-computing>. Servers belong to the group
unless further info is provided.

| Server name | GPUs | Storage info | Further info |
|---|---|---|---|
{% for i in site.data.gpu_resources -%}
{% if i.name -%}
|{{ i.name }} | {{ i.gpus }} | {{ i.storage }} | {{ i.info }}
{% endif %}
{%- endfor -%}
