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
    <div data-label="container" class="br_2 br_black-2 br_round br_solid flex flex_column isolate_isolation items_center m-x_5 relative">
    {% include_relative ACCNavigator/subs/question-header.html %}
    {%  include_relative ACCNavigator/subs/response-buttons-with-shuffle.html %}
        <main data-label="type-ahead-answers" class="p-x_6:lg  p-x_5:md p-x_4 p-y_6:md p-y_5 w_100 grid grid-col_4:lg grid-col_2:md grid-col_1 gap-x_5:lg gap-x_4:md gap-y_4">
            <h2 class="c_black-8 col-start_1 col-end_4:lg col-end_2:md col-end_1 self_center text_left font_accent">Text search for "Credit"</h2>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Earn Credits</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>See My Credits</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Print My Credits</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Find Credits</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Review Credits</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="bg_secondary-5 br_1 br_black-1 br_none br_radius br_solid c_black-8 col-start_last cursor_pointer ease_out f:outline_none font_medium font_ui h:bg_secondary-3 h:c_black h:undecorated inline-block row-start_1:md row-start_2 col-start_2:md col-start_4:lg text_center transition_1 w_auto" data-label="word-shuffle">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Clear Text</span>
                        <i class="far fa-times p-l_3 p-l_4:lg display_none:empty">
                            <icon></icon>
                        </i>
                    </div>
                </div>
            </a>
        </main>
        <main data-label="result-links" class="p-x_4 p-x_5:md p-x_6:lg p-y_5 p-y_6:md w_100">
            <h2 class="c_black-8 col-start_1 col-end_4:lg col-end_2:md col-end_1 self_center text_center font_accent">You can find <span class="c_accent-n1 font_bold uppercase">Credits</span> that are <span class="c_primary-n1 font_bold uppercase">ondemand</span>  here:</h2>
            <ul class="ul_none br-t_1 br_solid br_primary-n1">
                <li class="p-x_3 p-y_3 p-y_4:md br-b_1 br_solid br_primary-n1 flex flex_row relative">
                    <div class="flex_auto">
                     <h3 class="font_display font_medium"><a class="expanded-click-area">Title of the Page</a></h3>
                     <div data-label="breadcrumbs">
                         <ul class="flex flex_row font_ui justify_start lh_0 ul_none flex_wrap gap-x_3 lh_1">
                             <li class="flex_none">
                                 <i class="c_primary-n3 fa-home-alt fas m-r_2 self_baseline vertical-align_middle"></i>
                                 <span class="vertical-align_middle">Home</span>
                             </li>
                             <li class="flex_none">
                                 <i class="c_primary-n3 fa-caret-right  fas m-r_2 self_baseline vertical-align_middle"></i>
                                 <span class="vertical-align_middle">Page Parent</span>
                             </li>
                             <li class="flex_none">
                                 <i class="c_primary-n3 fa-caret-right  fas m-r_2 self_baseline vertical-align_middle"></i>
                                 <span class="vertical-align_middle">Page Name</span>
                             </li>
                         </ul>
                     </div>
                    </div>
                    <div class="flex_none grid justify_center items_center"> 
                        <i class="c_primary-n1 fa-arrow-alt-circle-right fas font-size_up-2 p-x_3 p-x_4:md"></i>
                        <span class="block:touch c_primary-n1 display_none font-size_down-2 font_bold lh_0 m-t_n3 text_center">Go To</span>
                     </div>               
                 </li>
                 <li class="p-x_3 p-y_3 p-y_4:md br-b_1 br_solid br_primary-n1 flex flex_row relative">
                    <div class="flex_auto">
                     <h3 class="font_display font_medium"><a class="expanded-click-area">Title of the Page</a></h3>
                     <div data-label="breadcrumbs">
                         <ul class="flex flex_row font_ui justify_start lh_0 ul_none flex_wrap gap-x_3 lh_1">
                             <li class="flex_none">
                                 <i class="c_primary-n3 fa-home-alt fas m-r_2 self_baseline vertical-align_middle"></i>
                                 <span class="vertical-align_middle">Home</span>
                             </li>
                             <li class="flex_none">
                                 <i class="c_primary-n3 fa-caret-right  fas m-r_2 self_baseline vertical-align_middle"></i>
                                 <span class="vertical-align_middle">Page Parent</span>
                             </li>
                             <li class="flex_none">
                                 <i class="c_primary-n3 fa-caret-right  fas m-r_2 self_baseline vertical-align_middle"></i>
                                 <span class="vertical-align_middle">Page Name</span>
                             </li>
                         </ul>
                     </div>
                    </div>
                    <div class="flex_none grid justify_center items_center"> 
                        <i class="c_primary-n1 fa-arrow-alt-circle-right fas font-size_up-2 p-x_3 p-x_4:md"></i>
                        <span class="block:touch c_primary-n1 display_none font-size_down-2 font_bold lh_0 m-t_n3 text_center">Go To</span>
                     </div>               
                 </li>
            </ul>
        </main>
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