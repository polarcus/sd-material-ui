# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Slider(Component):
    """A Slider component.
A Dash material-ui Paper component

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): Can be used to render elements inside the Slider
- id (string; optional): ID for Slider
- className (string; optional): The CSS class name of the root element
- classes (dict; optional): The classes to be applied to this component. classes has the following type: dict containing keys 'root', 'colorPrimary', 'colorSecondary', 'marked', 'vertical', 'disabled', 'rail', 'track', 'trackFalse', 'trackInverted', 'thumb', 'thumbColorPrimary', 'thumbColorSecondary', 'active', 'focusVisible', 'valueLabel', 'mark', 'markActive', 'markLabel', 'markLabelActive'.
  Those keys have the following types:
  - root (string; optional)
  - colorPrimary (string; optional)
  - colorSecondary (string; optional)
  - marked (string; optional)
  - vertical (string; optional)
  - disabled (string; optional)
  - rail (string; optional)
  - track (string; optional)
  - trackFalse (string; optional)
  - trackInverted (string; optional)
  - thumb (string; optional)
  - thumbColorPrimary (string; optional)
  - thumbColorSecondary (string; optional)
  - active (string; optional)
  - focusVisible (string; optional)
  - valueLabel (string; optional)
  - mark (string; optional)
  - markActive (string; optional)
  - markLabel (string; optional)
  - markLabelActive (string; optional)
- color (string; optional): The color of this slider
- component (string; optional): The component to be used
- defaultValue (string; optional): The default value of the slider
- disabled (boolean; default False): Disabled or not
- marks (list; optional): Marks
- max (string; optional): max
- min (string; optional): min
- step (number; optional)
- value (number; default 0)
- valueLabelDisplay (string; default 'on')"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, component=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, marks=Component.UNDEFINED, max=Component.UNDEFINED, min=Component.UNDEFINED, step=Component.UNDEFINED, value=Component.UNDEFINED, valueLabelDisplay=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'color', 'component', 'defaultValue', 'disabled', 'marks', 'max', 'min', 'step', 'value', 'valueLabelDisplay']
        self._type = 'Slider'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'color', 'component', 'defaultValue', 'disabled', 'marks', 'max', 'min', 'step', 'value', 'valueLabelDisplay']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Slider, self).__init__(children=children, **args)
