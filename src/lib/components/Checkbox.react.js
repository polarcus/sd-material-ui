// @flow

import React, {Component} from 'react';
import MuiCheckbox from '@material-ui/core/Checkbox';
import FormControlLabel from '@material-ui/core/FormControlLabel';
// import lightBaseTheme from 'material-ui/styles/baseThemes/lightBaseTheme';
// import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
// import getMuiTheme from 'material-ui/styles/getMuiTheme';
import polarcusTheme from '../polarcusTheme';
import {ThemeProvider} from '@material-ui/core';

type Props = {
    /** Checkbox is checked if true */
    checked?: boolean,
    /** CSS class name of the root element */
    className?: string,
    /** The classes to be applied to this component. This keys in this object must be valid CSS rule
     * names, and the values must be strings for the classnames to be assigned to each rule name
     * Valid rule names are:
     *   root
     *   checked
     *   disabled
     *   indeterminate
     *   colorPrimary
     *   colorSecondary
     */
    classes?: {
        root?: string,
        checked?: string,
        disabled?: string,
        indeterminate?: string,
        colorPrimary?: string,
        colorSecondary?: string,
        sizeSmall?: string,
    },
    /** Checkbox is disabled if true */
    disabled?: boolean,
    /** Ripple is disabled if true */
    disableRipple?: boolean,
    /** A callback for firing events to dash */
    fireEvent?: () => void,
    /** The element's ID */
    id: string,
    /** The label for the checkbox */
    label: string,
    /** The name prop of the checkbox */
    name: string,
    /** Dash callback to update props on the server */
    setProps?: () => void,
    /** Override the inline styles of the root element */
    style?: Object,
    /** The default color */
    color?: string,
};

type State = {
    checked: boolean,
};

const defaultProps = {
    checked: false,
    disabled: false,
    classes: {},
    disableRipple: false,
    fireEvent: () => {},
    setProps: () => {},
    style: {},
    className: null,
    name: '',
    label: null,
    color: 'primary',
};

/** Material UI Checkbox component */
export default class Checkbox extends Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {checked: props.checked};
    }

    UNSAFE_componentWillReceiveProps(nextProps: Props, nextContext: *): void {
        if (
            nextProps.checked !== null &&
            nextProps.checked !== this.props.checked
        ) {
            this.props.setProps({checked: nextProps.checked});
            this.setState({checked: nextProps.checked});
        }
    }

    handleClick = () => {
        const set_check = !this.state.checked;
        if (this.setState) this.setState({checked: set_check});
        if (this.props.setProps) this.props.setProps({checked: set_check});
        if (this.props.fireEvent) this.props.fireEvent({event: 'click'});
    };

    render() {
        const {
            disabled,
            style,
            classes,
            id,
            className,
            name,
            label,
            disableRipple,
            color,
        } = this.props;
        if (this.props.fireEvent || this.props.setProps) {
            this.handleClick = this.handleClick.bind(this);
            return (
                <div id={id} className={className}>
                    <ThemeProvider theme={polarcusTheme}>
                        <FormControlLabel
                            control={
                                <MuiCheckbox
                                    checked={this.state.checked}
                                    disabled={disabled}
                                    style={style}
                                    classes={classes}
                                    name={name}
                                    onChange={this.handleClick}
                                    color={color}
                                />
                            }
                            label={label}
                        />
                    </ThemeProvider>
                </div>
            );
        }
        return (
            <div id={id} className={className}>
                <ThemeProvider theme={polarcusTheme}>
                    <FormControlLabel
                        control={
                            <MuiCheckbox
                                checked={this.state.checked}
                                disabled={disabled}
                                disableRipple={disableRipple}
                                className={className}
                                style={style}
                                classes={classes}
                                name={name}
                                color={color}
                            />
                        }
                        label={label}
                    />
                </ThemeProvider>
            </div>
        );
    }
}

Checkbox.defaultProps = defaultProps;
