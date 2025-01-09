---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<h1>Collection in the Prototype Area</h1>
<hr>
<div class="reading-typography grid columns_6:lg columns_5:md gap_4:md gap_5:lg">
  <div class="col-start_1 col-end_3:md col-end_end">
  {% for collection in site.collections %}
    {% if collection.label == 'ui_gold_standard'  %}
    <div class="p_4 m-b_4  ">
      <h2 >{{ collection.label | replace: "_", " " | capitalize }}</h2>
      <ul class="ul_none font_1:lg font_0  grid gap_2 columns_1">
      {% for doc in collection.docs %}
        <li class="p_3 bg_black-1 h:bg_primary-5 m_0">
          <a class="not-link" href="{{ doc.url | append: site.github.build_revision | relative_url }}">
            <strong>{{ doc.name }}</strong>
            {% if doc.position %}
              <small class="opacity_7 block"> {{ doc.position }}</small>
            {% endif %}
          </a>
        </li>
      {% endfor %}
      </ul>
    </div>
    {% endif %}
    {% endfor %}
  </div>
  <div class="col-start_3:md col-start_start col-end_end grid columns_3:lg columns_2:md gap_4:md gap_5:lg">
    {% for collection in site.collections %}
    {% if collection.label != 'posts' and  collection.label != 'ui_gold_standard'  %}
    <div class="p_4 m-b_4  ">
      <h2 >{{ collection.label | replace: "_", " " | capitalize }}</h2>
      <ul class="ul_none grid gap_2 columns_1 font_1:lg font_0">
      {% for doc in collection.docs %}
        <li class="p_3 bg_black-1 h:bg_primary-5 m_0">
          <a class="not-link" href="{{ doc.url | append: site.github.build_revision | relative_url }}">
            <strong>{{ doc.name }}</strong>
            {% if doc.position %}
              <small class="opacity_7 block"> {{ doc.position }}</small>
            {% endif %}
          </a>
        </li>
      {% endfor %}
      </ul>
    </div>
    {% endif %}
    {% endfor %}
  </div>
</div>
