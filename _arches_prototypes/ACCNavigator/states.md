## States of the Widtget

* [First Quesion Answer](#first-quesion-answer)
* [Follow-up Question Answer](#follow-up-question-answwer)
* [Result State](#result-state)
* [Empty or Onload State](#empty-or-onload-state)
* [Power User Feature](#power-user-feature)

### First Quesion Answer

The ACC Navigator **(Widget)**  shows the question of "I want to" with an input-line-response and a collection of response buttons populated with response-terms pulled from our search term-result-pairs in SiteCore.  The response-terms will be appropriate to the questions and the lists order will be randomized.  The rendered response buttons are limited to a max count and if the appropriate responses are more then the max count the system will render a shuffle button. 

When the user hits the shuffle button the current list of response buttons will be transition out and the next set of response buttons will be displayed.  If the shuffle mechanism reaches the end of the response list then the system will loop to the beginning of the list.  

If the user types into the response line then trigger the [`Power User Feature`](#power-user-feature)

When the user clicks a response button  the response line will be replaced but the selected response button. The system will progress the next state either a [`Follow-up Qestion State`](#follow-up-question-answwer) or a [`Result State`](#result-state) depending if the response-term has follow up terms or can match to a result. 

<section data-label="acc-navigator" class="m-y_6 font_n1 font_0:md font_1:lg">
    <div data-label="container" class="br_2 br_black-2 br_round br_solid flex flex_column isolate_isolation items_center m-x_5 relative">
        <header class="font-size_up-2 font_accent font_medium inline-block isolate_isolation overflow_visible w_auto t_n2 m-t_n4 w_100">
            <div class="flex flex_wrap flex_row:md flex_column items_center justify_center z_1 p-x_5:lg p-x_4:md p-x_3 gap-y_4">
                <div data-label="sentence-starter" class="flex_none self_center lh_0 p-x_4 bg_white">I want to</div>
                <div data-label="ask-word-first" class="bg_white grid justify_center justify_end max-w_40 p-y_2 self_stretch w_100" style="
    justify-content: stretch;
">
                    <div data-label="input-wrapper" class="flex flex_column justify_center m-t_n5 m-x_4 relative self_stretch transition_3 w_auto">
                        <input type="text" name="" id="input-word-first" class="bg_transparent br-b_2 br_0 br_accent br_solid br_square f:none font-size_up lh_1 opacity_none overflow_visible p-r_4 relative self_stretch text_center w_auto">
                        <i class="absolute b_0 c_black-4 fa-times fas font-size_down-2 grid h:c_black items_center just justify_center p_3 r_n3 t_0"></i>
                    </div>
                </div>
            </div>
        </header>
        <main data-label="shuffle-answers" class="p-x_6:lg  p-x_5:md p-x_4 p-y_6:md p-y_5 w_100 grid grid-col_4:lg grid-col_2:md grid-col_1 gap-x_6:lg gap-x_4:md gap-y_4">
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Button</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Button</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_accent-n2 h:c_black h:bg_accent-3 bg_accent-4 br_black-1 cursor_pointer br_1 br_solid br_radius flex_30" data-label="select-word-first">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Button</span>
                        <i class="p-l_3 p-l_4:lg display_none:empty"></i>
                    </div>
                </div>
            </a>
            <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_black-8 h:c_black h:bg_secondary-3 bg_secondary-5 br_black-1 cursor_pointer br_1 br_solid br_radius" data-label="word-shuffle">
                <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                    <div class="flex_auto self_center justify_center flex">
                        <span>Shuffle</span>
                        <i class="far fa-sync p-l_3 p-l_4:lg display_none:empty">
                            <icon></icon>
                        </i>
                    </div>
                </div>
            </a>
        </main>
        <footer class="absolute font_accent font_medium flex flex_row h_0 items_center justify_center b_0 w_auto">
            <div class="bg_white flex flex_nowrap flex_row gap_4 items_center justify_around p-x_3 p-x_4:md p-x_5:lg w_auto z_1">
                <a class="ease_out h:undecorated transition_1 f:outline_none text_center br_none inline-block w_auto font_medium font_ui  c_black-8 h:c_black h:bg_secondary-3 bg_secondary-5 br_black-1 cursor_pointer br_1 br_solid br_radius" data-label="sentence-reset">
                    <div class="flex block justify_center flex_column p-y_3 p-x_3 p-x_5:lg lh_0 p-y_4:md">
                        <div class="flex_auto self_center justify_center flex">
                            <span>Reset Question</span>
                            <i class="far fa-times p-l_3 p-l_4:lg display_none:empty">
                                <icon></icon>
                            </i>
                        </div>
                    </div>
                </a>
            </div>
        </footer>
    </div>
</section>


### Follow-up Question Answwer

The Follow-up requires the system to revalutate the term-result-pairs filtered by the previous response. If the response list is singluar it will auto fill the only result and proceed to the [`Result State`](#result-state). If the result list is greater then one then the system will render the follow up question line, and the response buttons with the shuffle button if needed. The system will also render a `Restart Question` button bellow the response and suffle buttons. 

The shuffle button works the same as it does with the previous state just will a smaller response list.

If the user types into the response line then trigger the [`Power User Feature`](#power-user-feature)

If the user clicks the `Restart Question` Button the Widget will return to a [`Empty or Onload State`](#empty-or-onload-state).

### Result State

When the widget has only results and or no extra follow-up responses the system will show the result view. The resul view is a list of pages or items from the filtered term-result-pairs list.

Each result will render the Page Title, and a how to navigate to this page breadcrumb to the item from the widgets location.

## Psydo State or Features

### Empty or Onload State

The ACC Navigator **(Widget)** when onload and there are no query strings to the URL the widget will render the `First Question Answer` 

### Power User Feature