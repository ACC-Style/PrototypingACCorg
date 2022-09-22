- [States of the Widget](#states-of-the-widget)
  - [First Question Answer](#first-question-answer)
  - [Follow-up Question Answer](#follow-up-question-answer)
  - [Result State](#result-state)
- [Pseudo State or Features](#pseudo-state-or-features)
  - [Empty or Onload State](#empty-or-onload-state)
  - [Power User Feature](#power-user-feature)
- [Admin & Analytics](#admin--analytics)
  - [Admins How to Populate ACC Navigator](#admins-how-to-populate-acc-navigator)
  - [Analytics](#analytics)
    - [Sample Data](#sample-data)

## States of the Widget





----------


### First Question Answer

The ACC Navigator **(Widget)** shows the question of "I want to" with an input-line-response and a collection of response buttons populated with response-terms pulled from our search term-result-pairs in SiteCore. The response-terms will be appropriate to the questions and the lists order will be randomized. The rendered response buttons are limited to a max count and if the appropriate responses are more then the max count the system will render a shuffle button.

When the user hits the shuffle button the current list of response buttons will be transition out and the next set of response buttons will be displayed. If the shuffle mechanism reaches the end of the response list then the system will loop to the beginning of the list.

If the user types into the response line then trigger the [`Power User Feature`](#power-user-feature)

When the user clicks a response button the response line will be replaced but the selected response button. The system will progress the next state either a [`Follow-up Question State`](#follow-up-question-answer) or a [`Result State`](#result-state) depending if the response-term has follow up terms or can match to a result.

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

### Follow-up Question Answer

The Follow-up UI is decorated different then the first round questions to denote a change to the user and to help clue them into which UI is effected but the new UI.

The Follow-up requires the system to revaluate the term-result-pairs filtered by the previous response. If the response list is singular it will auto fill the only result and proceed to the [`Result State`](#result-state). If the result list is greater then one then the system will render the follow up question line, and the response buttons with the shuffle button if needed. The system will also render a `Restart Question` button bellow the response and shuffle buttons.

The shuffle button works the same as it does with the previous state just will a smaller response list.

If the user types into the response line then trigger the [`Power User Feature`](#power-user-feature)

If the user clicks the `Restart Question` Button the Widget will return to a [`Empty or Onload State`](#empty-or-onload-state).

<section data-label="acc-navigator" class="m-y_6 font_n1 font_0:md font_1:lg">
    <div data-label="container" class="br_2 br_black-2 br_round br_solid flex flex_column isolate_isolation items_center m-x_5 relative">
    <header class="font-size_up-2 font_accent font_medium isolate_isolation overflow_visible grid justify_center items_center" style="translate: 0 -50%;">
  	  <div id="question-line" class="flex flex_wrap flex_row items_center justify_center z_1 p-x_5:lg p-x_4:md p-x_4 gap-y_4 bg_white w_auto">
  		  <div data-label="sentence-starter" class="flex_none self_center lh_0 p-x_4 bg_white">I want to</div>
        {% include_relative ACCNavigator/subs/result-button.html %}
        <div data-label="sentence-bridge" class="flex_none self_center lh_0 p-x_4 bg_white">that are</div>
        {% include_relative ACCNavigator/subs/follow-up_question-line.html %}
      </div>
      </header>
    {%  include_relative ACCNavigator/subs/follow-up_response-buttons-with-shuffle.html %}
    {% include_relative ACCNavigator/subs/reset-question-footer.html %}
    </div>
</section>

### Result State

When the widget has only results and or no extra follow-up responses the system will show the result view. The resul view is a list of pages or items from the filtered term-result-pairs list.

Each result will render the Page Title, and a how to navigate to this page breadcrumb to the item from the widgets location.

<section data-label="acc-navigator" class="m-y_6 font_n1 font_0:md font_1:lg">
    <div data-label="container" class="br_2 br_black-2 br_round br_solid flex flex_column isolate_isolation items_center m-x_5 relative">
    <header class="font-size_up-2 font_accent font_medium isolate_isolation overflow_visible grid justify_center items_center" style="translate: 0 -50%;">
  	  <div id="question-line" class="flex flex_wrap flex_row items_center justify_center z_1 p-x_5:lg p-x_4:md p-x_4 gap-y_4 bg_white w_auto">
  		  <div data-label="sentence-starter" class="flex_none self_center lh_0 p-x_4 bg_white">I want to</div>
        {% include_relative ACCNavigator/subs/result-button.html %}
        <div data-label="sentence-bridge" class="flex_none self_center lh_0 p-x_4 bg_white">that are</div>
        {% include_relative ACCNavigator/subs/follow-up_result-button.html %}
      </div>
      </header>
    {%  include_relative ACCNavigator/subs/result-list.html %}
    {% include_relative ACCNavigator/subs/reset-question-footer.html %}
    </div>
</section>

----------

## Pseudo State or Features

### Empty or Onload State

The ACC Navigator **(Widget)** when onload and there are no query strings to the URL the widget will render the `First Question Answer`

----------

### Power User Feature

The user should be able to type in question line.  This will replace the basic response buttons and shuffle button with a grid of buttons based on a reductive filter of the users typed text.  For example typed text of `credit` will return all buttons with `credit` in their label.  A `clear text` button appears in the top right of the button grid and an X button at the end of the text input.   Clicking either will return the user to the basic mode of the current state of the widget and clear out any text in the question-line.  Clicking any of the response buttons will  replace the question line at the top with the selected response button and will progress the widget to the next state.

<section data-label="acc-navigator" class="m-y_6 font_n1 font_0:md font_1:lg">
    <div data-label="container" class="br_2 br_black-2 br_round br_solid flex flex_column isolate_isolation items_center m-x_5 relative">
    <header class="font-size_up-2 font_accent font_medium isolate_isolation overflow_visible grid justify_center items_center" style="translate: 0 -50%;">
    	<div id="question-line" class="flex flex_wrap flex_row items_center justify_center z_1 p-x_5:lg p-x_4:md p-x_4 gap-y_4 bg_white w_auto">
    		<div data-label="sentence-starter" class="flex_none self_center lh_0 p-x_4 bg_white">I want to</div>
        <div data-element="question-line" data-label="ask-word" class="flex_auto isolate_isolation flex_20 max-w_15">
        	<div data-label="input-wrapper" class="flex flex_row flex_nowrap justify_center relative transition_3 w_auto">
        		<input type="text" name="" id="input-word-first" class="bg_transparent br-b_2 br_0 br_accent br_solid br_square f:none font-size_up opacity_none overflow_visible p-r_4 relative text_center z_1" value="Credit">
        		<button  class="flex_none c_black-4 font-size_down-2 r_n3 h:c_black p_3 br_none bg_transparent m-l_n5 z_2"><i class="fas fa-times"></i></button>
        	</div>
        </div>
      </div>
    </header>
    {% include_relative ACCNavigator/subs/power-user_type-ahead.html %}  
    {% include_relative ACCNavigator/subs/cancel-type-ahead-footer.html %}  
    </div>
</section>

----------



## Admin & Analytics
### Admins How to Populate ACC Navigator

This is still being discussed but the current concept is to extend the meta data on pages to allow for adding result sentences to page. Result sentences would be a combination of first word, sentence bridge and second word. Sentence Gap, and Second word is Optional.

The admins should be able to create, repeat, update and delete the result sentences on a page or content. 

<p class="text_center"><span class="c_highlight m-x_auto inline-block">! This UI is for demo purposes only !</span></p>
<div class="m_4 br_radius bg_black-05 p_4 shadow_overlap-light">
<h4 class="">ACC Navigator Meta Data</h4>
<table class="m-t_3 br_1 br_radius br_black-3 br_solid table table-striped table-bordered">
  <thead>
    <tr>
      <th>First Word</th>
      <th>Sentence Gap</th>
      <th>Second Word</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Credit</td>
      <td>that are</td>
      <td>On Demand</td>
      <td class="text_right"><a href="#" class="btn btn-alert btn-sm c_white">remove</a></td>
    </tr>
    <tr>
      <td>Learn</td>
      <td>about</td>
      <td>Afib</td>
      <td class="text_right"><a href="#" class="btn btn-alert btn-sm c_white">remove</a></td>
    </tr>
    <tr>
      <td>AFIBSap</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td class="text_right"><a href="#" class="btn btn-alert btn-sm c_white">remove</a></td>
    </tr>
  </tbody>
</table>
<div class="m-t_5 p_4 br_round bg_black-1 shadow_emboss-light">
<h5 class="">Add Meta Data To Page</h5>
<div class="flex flex_row gap_4 items_end justify_between m-x_4">
<div>
<div class="m-b_3"><label class="m-b_3" for="example-input-email">First Word <sup><i class="fas fa-asterisk c_warning"></i></sup></label> <input type="text" id="example-input-email" placeholder=""></div></div>
<div><div class="m-b_3"><label class="m-b_3" for="example-input-email">Email address</label> <input type="text" id="example-input-email" placeholder=""></div></div>
<div><div class="m-b_3"><label class="m-b_3" for="example-input-email">Second Word</label> <input type="text" id="example-input-email" placeholder=""></div></div></div>
<div class="flex flex_row-reverse gap_4 items_end justify_between m-x_4"><a href="" class="btn btn-primary c_white"><i class="fas fas-solid fa-plus"></i> Add Another</a><span class="c_warning "><sup><i class="fas fa-asterisk c_warning"></i> </sup>required</span></div>
</div>
</div>

----------
### Analytics

This system should either through google or a log system track how a the user completes a result or where it is abandoned. Abandoned is defined when the user restarts the widget.

#### Sample Data

`Date, Success , First Word, Second Word, Result Clicked On`

----------