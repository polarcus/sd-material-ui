# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TextField(Component):
    """A TextField component.
A Dash material-ui TextField component

Keyword arguments:
- id (string; required): ID for TextField
- className (string; optional): The CSS class name of the root element
- classes (dict; optional): The classes to be applied to this component. classes has the following type: dict containing keys 'root'.
  Those keys have the following types:
  - root (string; optional)
- color (string; default 'primary'): Color - primary or secondary
- defaultValue (string; optional): The default value
- fullWidth (boolean; default False): Take up fill width of container
- helperText (a list of or a singular dash component, string or number; optional): The helper text
- label (a list of or a singular dash component, string or number; optional): The label content
- placeholder (string; optional): Placeholder text
- value (bool | number | str | dict | list; optional): Value of the input
- variant (default 'outlined'): The variant"""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, className=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, defaultValue=Component.UNDEFINED, fullWidth=Component.UNDEFINED, helperText=Component.UNDEFINED, label=Component.UNDEFINED, placeholder=Component.UNDEFINED, value=Component.UNDEFINED, variant=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'classes', 'color', 'defaultValue', 'fullWidth', 'helperText', 'label', 'placeholder', 'value', 'variant']
        self._type = 'TextField'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'classes', 'color', 'defaultValue', 'fullWidth', 'helperText', 'label', 'placeholder', 'value', 'variant']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TextField, self).__init__(**args)
