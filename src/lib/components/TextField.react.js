// @flow

import React, {Component} from 'react';
import polarcusTheme from '../polarcusTheme';
import {ThemeProvider} from '@material-ui/core';
import MuiTextField from '@material-ui/core/TextField';

type Props = {
    /** ID for TextField */
    id: string,
    /** The CSS class name of the root element */
    className?: string,
    /** The classes to be applied to this component. */
    classes?: {
        root?: string,
    },
    /** Color - primary or secondary*/
    color?: string,
    /** The default value */
    defaultValue?: string,
    /** Take up fill width of container */
    fullWidth?: boolean,
    /** The helper text */
    helperText?: Node,
    /** The label content */
    label?: Node,
    /** Placeholder text */
    placeholder?: string,
    /** Value of the input */
    value?: any,
    /** The variant */
    variant?: 'filled' | 'outlined' | 'standard',
};

const defaultProps = {
    className: null,
    classes: {},
    defaultValue: null,
    color: 'primary',
    fullWidth: false,
    helperText: null,
    label: null,
    placeholder: null,
    value: null,
    variant: 'outlined',
};

/** A Dash material-ui TextField component */
export default class TextField extends Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {value: props.value};
    }

    // handleChange = (event) => {
    //     this.setState({value: event.target.value});
    //     if (typeof this.props.setProps === 'function') {
    //         this.props.setProps({value: event.target.value});
    //     }
    // };

    render() {
        const {
            id,
            className,
            classes,
            color,
            defaultValue,
            fullWidth,
            helperText,
            label,
            placeholder,
            value,
            variant,
        } = this.props;

        return (
            <ThemeProvider theme={polarcusTheme}>
                <MuiTextField
                    id={id}
                    className={className}
                    classes={classes}
                    color={color}
                    defaultValue={defaultValue}
                    fullWidth={fullWidth}
                    helperText={helperText}
                    label={label}
                    placeholder={placeholder}
                    value={value}
                    variant={variant}
                    onChange={this.handleChange}
                />
            </ThemeProvider>
        );
    }
}

TextField.defaultProps = defaultProps;
