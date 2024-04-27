---
layout: page
permalink: /rota/
redirect_from:
  - /rota.html
  - /rota
title: Rota
---

|Week commencing  | Group meeting presenter (Weds 5pm)  | Reading group presenter (Thurs 4pm) |
|---|---|---|
{% for i in site.data.rota_names -%}
{% if i.week_date -%}
|{{ i.week_date }} | {{ i.group }} | {{ i.reading }}  |
{% endif %}
{%- endfor -%}
