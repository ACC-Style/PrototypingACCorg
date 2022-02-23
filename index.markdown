---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
<div class="grid grid-col_3:lg grid-col_2:md grid-col_1 gap_4">

<div class="">
<h2 class="font_display">Legacy Prototypes</h2>
{% for legacy_prototype in site.legacy_prototypes %}
  <ul class="ul_none ">
<li class="p_3 p-l_0 h:bg_primary-5">    <a href="{{ legacy_prototype.url | append: site.github.build_revision | relative_url }}">
      {{ legacy_prototype.name }} - {{ legacy_prototype.position }}
    </a></li>
  </ul>
{% endfor %}
</div>
<div class="">
<h2 class="font_display">Arches Prototypes</h2>
{% for arches_prototype in site.arches_prototypes %}
  <ul class="ul_none ">
<li class="p_3 p-l_0 h:bg_primary-5">    <a href="{{ arches_prototype.url | append: site.github.build_revision | relative_url }}">
      {{ arches_prototype.name }} - {{ arches_prototype.position }}
    </a></li>
  </ul>
{% endfor %}
</div>
<div class="">
<h2 class="font_display">Virtual Prototypes</h2>
{% for virtual_prototype in site.virtual_prototypes %}
  <ul class="ul_none ">
<li class="p_3 p-l_0 h:bg_primary-5">    <a href="{{ virtual_prototype.url | append: site.github.build_revision | relative_url }}">
      {{ virtual_prototype.name }} - {{ virtual_prototype.position }}
    </a></li>
  </ul>
{% endfor %}
</div>
<div class="">
<h2 class="font_display">Federated Login Prototypes</h2>
{% for fedlogin_prototype in site.fedlogin_prototypes %}
  <ul class="ul_none ">
<li class="p_3 p-l_0 h:bg_primary-5">    <a href="{{ fedlogin_prototype.url | append: site.github.build_revision | relative_url }}">
      {{ fedlogin_prototype.name }}
      {% if fedlogin_prototype.position %}
         - {{ fedlogin_prototype.position }}
      {% endif %}
    </a></li>
  </ul>
{% endfor %}
</div>
<div class="">
<h2 class="font_display">Library Prototypes</h2>
{% for library_prototype in site.library_prototypes %}
  <ul class="ul_none ">
<li class="p_3 p-l_0 h:bg_primary-5">    <a href="{{ library_prototype.url | append: site.github.build_revision | relative_url }}">
      {{ library_prototype.name }}
      {% if library_prototype.position %}
         - {{ library_prototype.position }}
      {% endif %}
    </a></li>
  </ul>
{% endfor %}
</div>
<div class="">
<h2 class="font_display">Event Prototypes</h2>
{% for event_prototype in site.event_prototypes %}
  <ul class="ul_none ">
<li class="p_3 p-l_0 h:bg_primary-5">    <a href="{{ event_prototype.url | append: site.github.build_revision | relative_url }}">
      {{ event_prototype.name }}
      {% if event_prototype.position %}
         - {{ event_prototype.position }}
      {% endif %}
    </a></li>
  </ul>
{% endfor %}
</div>
</div>
