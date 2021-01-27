// @flow
import React, {Component} from 'react';
import polarcusTheme from '../polarcusTheme';
import {ThemeProvider} from '@material-ui/core';

type Props = {
    /** ID for ColorPicker */
    id?: string,
    /** The initial value of the color picker */
    value?: number,
    /** To dipslay the label for the selected color */
    displayLabel?: boolean,
};

type State = {
    value?: number,
    displayLabel?: boolean,
};

const defaultProps = {
    id: null,
    value: '#000000',
    displayLabel: true,
};

/** A Dash Color Picker component */

export default class ColorPicker extends Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {value: props.value, displayLabel: props.displayLabel};
    }

    handleChange = (e) => {
        this.setState({value: e.target.value});
        if (typeof this.props.setProps === 'function') {
            this.props.setProps({value: e.target.value});
        }
    };

    render() {
        const {id, value, displayLabel} = this.props;

        return (
            <div id={id}>
                <ThemeProvider theme={polarcusTheme}>
                    <input
                        type="color"
                        value={value}
                        onChange={this.handleChange}
                    />
                    {displayLabel && (
                        <span
                            className="colorPicker-displayLabel"
                            style={{marginLeft: 4}}
                        >
                            {value}
                        </span>
                    )}
                </ThemeProvider>
            </div>
        );
    }
}

ColorPicker.defaultProps = defaultProps;
