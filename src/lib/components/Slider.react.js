// @flow

import React, {Component} from 'react';
import polarcusTheme from '../polarcusTheme';
import MuiSlider from '@material-ui/core/Slider';
import {ThemeProvider} from '@material-ui/core';

type Props = {
    /** ID for Slider */
    id?: string,
    /** Can be used to render elements inside the Slider*/
    children?: Node,
    /** The CSS class name of the root element */
    className?: string,
    /** The classes to be applied to this component */
    classes?: {
        root?: string,
        colorPrimary?: string,
        colorSecondary?: string,
        marked?: string,
        vertical?: string,
        disabled?: string,
        rail?: string,
        track?: string,
        trackFalse?: string,
        trackInverted?: string,
        thumb?: string,
        thumbColorPrimary?: string,
        thumbColorSecondary?: string,
        active?: string,
        focusVisible?: string,
        valueLabel?: string,
        mark?: string,
        markActive?: string,
        markLabel?: string,
        markLabelActive?: string,
    },
    /** The color of this slider */
    color?: string,
    /** The component to be used */
    component?: string,
    /** The default value of the slider */
    defaultValue?: string,
    /** Disabled or not */
    disabled?: boolean,
    /** Marks */
    marks?: Array<Object>,
    /** max */
    max?: string,
    /** min */
    min?: string,
    step?: number,
    value?: number | Array<number>,
    valueLabelDisplay?: string,
};

type State = {
    disabled: boolean,
    value: any,
};

const defaultProps = {
    children: null,
    classes: {},
    className: null,
    id: null,
    disabled: false,
    value: 0,
    valueLabelDisplay: 'on',
};

/** A Dash material-ui Paper component */
export default class Slider extends Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {disabled: props.disabled, value: props.value};
    }

    handleChange = (event, newValue) => {
        this.setState({value: newValue});
        if (typeof this.props.setProps === 'function') {
            this.props.setProps({value: newValue});
        }
    };

    render() {
        const {
            value,
            min,
            max,
            step,
            id,
            className,
            classes,
            valueLabelDisplay,
            marks,
        } = this.props;

        return (
            <div id={id}>
                <ThemeProvider theme={polarcusTheme}>
                    <MuiSlider
                        classes={classes}
                        className={className}
                        value={value}
                        min={min}
                        step={step}
                        max={max}
                        onChangeCommitted={this.handleChange}
                        valueLabelDisplay={valueLabelDisplay}
                        marks={marks}
                        // scale={(x) => x ** 10}
                        // getAriaValueText={valueLabelFormat}
                        // valueLabelFormat={valueLabelFormat}
                        // onChange={handleChange}
                        // valueLabelDisplay="auto"
                        // aria-labelledby="non-linear-slider"
                    />
                </ThemeProvider>
            </div>
        );
    }
}

Slider.defaultProps = defaultProps;
