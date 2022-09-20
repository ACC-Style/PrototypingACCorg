## States of the Widtget

- [States of the Widtget](#states-of-the-widtget)
  - [First Quesion Answer](#first-quesion-answer)
  - [Follow-up Question Answwer](#follow-up-question-answwer)
  - [Result State](#result-state)
- [Psydo State or Features](#psydo-state-or-features)
  - [Empty or Onload State](#empty-or-onload-state)
  - [Power User Feature](#power-user-feature)

### First Quesion Answer

The ACC Navigator **(Widget)**  shows the question of "I want to" with an input-line-response and a collection of response buttons populated with response-terms pulled from our search term-result-pairs in SiteCore.  The response-terms will be appropriate to the questions and the lists order will be randomized.  The rendered response buttons are limited to a max count and if the appropriate responses are more then the max count the system will render a shuffle button. 

When the user hits the shuffle button the current list of response buttons will be transition out and the next set of response buttons will be displayed.  If the shuffle mechanism reaches the end of the response list then the system will loop to the beginning of the list.  

If the user types into the response line then trigger the [`Power User Feature`](#power-user-feature)

When the user clicks a response button  the response line will be replaced but the selected response button. The system will progress the next state either a [`Follow-up Qestion State`](#follow-up-question-answwer) or a [`Result State`](#result-state) depending if the response-term has follow up terms or can match to a result. 

<section data-label="acc-navigator" class="m-y_6 font_n1 font_0:md font_1:lg">
    <div data-label="container" class="br_2 br_black-2 br_round br_solid flex flex_column isolate_isolation items_center m-x_5 relative">
    <header class="font-size_up-2 font_accent font_medium isolate_isolation overflow_visible grid justify_center items_center" style="translate: 0 -50%;">
    	<div id="question-line" class="flex flex_wrap flex_row items_center justify_center z_1 p-x_5:lg p-x_4:md p-x_4 gap-y_4 bg_white w_auto">
    		<div data-label="sentence-starter" class="flex_none self_center lh_0 p-x_4 bg_white">I want to</div>
                {% include_relative ACCNavigator/subs/question-line.html %}
            </div>
        </header>
{%  include_relative ACCNavigator/subs/response-buttons-with-shuffle.html %}
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