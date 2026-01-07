--- 
layout: arches 
name: "ACC Navigator" 
position: "Requirements" 
--- 


{% include_relative ACCNavigator/intro.md %}

<hr>

{% include_relative ACCNavigator/states.md %}


<hr>
<h2>Full Pattern</h2>
<section data-label="acc-navigator" class="m-y_6 font_n1 font_0:md font_1:lg">
    <div data-label="container" class="br_2 br_black-2 br_round br_solid flex flex_column isolation_isolate items_center m-x_5 relative">
    {% include_relative ACCNavigator/subs/question-header-all.html %}
    {%  include_relative ACCNavigator/subs/response-buttons-with-shuffle.html %}
    {% include_relative ACCNavigator/subs/power-user_type-ahead.html %}     
    {% include_relative ACCNavigator/subs/result-list.html %}  
    {% include_relative ACCNavigator/subs/reset-question-footer.html %}
    </div>
</section>
<style lang="css">
    .f\:none:focus {
        box-shadow: none !important;
        outline-color: none !important;
        outline: 0;
    }
</style>