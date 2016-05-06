#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from tornado_uifields import BaseUIModule

DAYS_OF_WEEK = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
               'Sep', 'Oct', 'Nov', 'Dec']


class SemanticUIBaseUIModule(BaseUIModule):
    name = ''
    label = ''
    value = ''
    css = ''
    trans = True
    form = {}
    default = ''
    extra = ''
    placeholder = ''


class TextField(SemanticUIBaseUIModule):
    template = 'semanticui/text_field.html'
    text_type = 'text'


class TextAreaField(SemanticUIBaseUIModule):
    template = 'semanticui/textarea_field.html'
    rows = 3


class SubmitButtonsField(SemanticUIBaseUIModule):
    template = 'semanticui/submit_buttons.html'
    url = ''
    url_name = 'home'
    cancel_label = 'Cancel'
    or_label = 'or'
    submit_label = 'Submit'
    cancel_css = ''
    submit_css = 'positive'
    loading_css = 'loading-link'


class DropdownBase(SemanticUIBaseUIModule):
    default_text = ''
    selections = []
    selected = ''
    dw_css = 'search'


class DropdownField(DropdownBase):
    template = 'semanticui/dropdown_field.html'


class MultiDropdownField(DropdownBase):
    template = 'semanticui/multi_dropdown_field.html'


class CheckboxField(SemanticUIBaseUIModule):
    template = 'semanticui/checkbox_field.html'
    checked = False
    read_only = False
    disabled = False


class RadioField(SemanticUIBaseUIModule):
    template = 'semanticui/radio_field.html'
    checked_idx = -1
    labels = []
    css = 'inline'


class Datepicker(SemanticUIBaseUIModule):
    template = 'semanticui/datepicker_field.html'
    id = 'input[name="daterange"]'
    single = 'true'
    show_dropdowns = 'true'
    show_weeks = 'true'
    show_time = 'false'
    show_seconds = 'false'
    start_date = ''
    end_date = ''
    min_date = ''
    max_date = ''
    hours_12 = 'true'
    timezone = ''
    date_format = 'YYYY-MM-DD'
    apply_class = 'positive'
    apply_label = 'Apply'
    cancel_label = 'Cancel'
    from_label = 'From'
    to_label = 'To'
    week_label = 'WK'
    custom_range_label = 'Custom Range'
    first_day = 1
    days_of_week = DAYS_OF_WEEK
    month_names = MONTH_NAMES


class AjaxDropdown(SemanticUIBaseUIModule):
    template = 'semanticui/dropdown_ajax.html'
    id1 = '#id1'
    id2 = '#id2'
    url_name = ''
    id2_default_text = ''
    single = True
