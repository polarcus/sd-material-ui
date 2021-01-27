# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ColorPicker(Component):
    """A ColorPicker component.
A Dash Color Picker component

Keyword arguments:
- id (string; optional): ID for ColorPicker
- value (number; default '#000000'): The initial value of the color picker
- displayLabel (boolean; default True): To dipslay the label for the selected color"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, displayLabel=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'displayLabel']
        self._type = 'ColorPicker'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'displayLabel']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ColorPicker, self).__init__(**args)
