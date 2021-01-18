// @flow

import React, {Component} from 'react';
import MUIButton from '@material-ui/core/Button';
import MUIIconButton from '@material-ui/core/IconButton';
import polarcusTheme from '../polarcusTheme';
// import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {ThemeProvider} from '@material-ui/core';

type Props = {
    /**
     * This is what will be displayed inside the button.
     * If a label is specified, the text within the label prop will
     * be displayed. Otherwise, the component will expect children
     * which will then be displayed. (In our example,
     * we are nesting an `<input type="file" />` and a `span`
     * that acts as our label to be displayed.) This only
     * applies to flat and disableShadow buttons.
     */
    children?: Node,
    /** The classes to be applied to this component. This keys in this object must be valid CSS rule
     * names, and the values must be strings for the classnames to be assigned to each rule name
     * Valid rule names are:
     *   root
     *   label
     *   text
     *   textPrimary
     *   textSecondary
     *   outline
     *   outlinedPrimary
     *   outlinedSecondary
     *   contained
     *   containedPrimary
     *   containedSecondary
     *   disableElevation
     *   focusVisible
     *   disabled
     *   colorInherit
     *   textSizeSmall
     *   textSizeLarge
     *   outlinedSizeSmall
     *   outlinedSizeLarge
     *   containedSizeSmall
     *   containedSizeLarge
     *   sizeSmall
     *   sizeLarge
     *   fullWidth
     *   startIcon
     *   endIcon
     *   iconSizeSmall
     *   iconSizeMedium
     *   iconSizeLarge
     *
     *   OR
     *
     *   root
     *   edgeStart
     *   edgeEnd
     *   colorInherit
     *   colorPrimary
     *   colorSecondary
     *   disabled
     *   sizeSmall
     *   label
     *
     * See https://material-ui.com/api/button/#css
     * and https://material-ui.com/api/icon-button/#css*/
    classes?: {
        root?: string,
        label?: string,
        text?: string,
        textPrimary?: string,
        textSecondary?: string,
        outline?: string,
        outlinedPrimary?: string,
        outlinedSecondary?: string,
        contained?: string,
        containedPrimary?: string,
        containedSecondary?: string,
        disableElevation?: string,
        focusVisible?: string,
        disabled?: string,
        colorInherit?: string,
        textSizeSmall?: string,
        textSizeLarge?: string,
        outlinedSizeSmall?: string,
        outlinedSizeLarge?: string,
        containedSizeSmall?: string,
        containedSizeLarge?: string,
        sizeSmall?: string,
        sizeLarge?: string,
        fullWidth?: string,
        startIcon?: string,
        endIcon?: string,
        iconSizeSmall?: string,
        iconSizeMedium?: string,
        iconSizeLarge?: string,
    },
    /** CSS class name of the root element */
    className?: string,
    /** If true, the element's ripple effect will be disabled */
    disableTouchRipple?: boolean,
    /** Disable the button? */
    disabled?: boolean,
    /** Dash callback to trigger an event handler */
    fireEvent?: () => void,
    /** If true, the button will take up the full width of its container */
    fullWidth?: boolean,
    /** The URL to link to when the button is clicked */
    href?: string,
    /** Sets the class of a span element inside the button */
    iconClass?: Node,
    /** Element ID */
    id?: string,
    /** An integer that represents the number fo times that this element has been clicked */
    n_clicks?: number,
    /** An integer that represents the previous number of times this element has been clicked */
    n_clicks_previous?: number,
    /** Hide the shadow behind the button */
    disableShadow?: string,
    /** Dash callback to update props */
    setProps?: () => void,
    /** Override the inline styles of the root element */
    style?: Object,
    /** If true, this object is rendered as an IconButton */
    useIcon?: boolean,
    /** 'contained' | 'outlined' | 'text', Button type if not an IconButton */
    variant?: string,
    /** 'primary' | 'secondary', Color of button */
    color?: string,
};

type State = {
    disabled: boolean,
    n_clicks: number,
    n_clicks_previous: number,
};

const defaultProps = {
    children: null,
    classes: {},
    className: '',
    disableTouchRipple: false,
    disabled: false,
    fireEvent: () => {},
    fullWidth: false,
    href: '',
    iconClass: null,
    n_clicks: 0,
    n_clicks_previous: 0,
    setProps: () => {},
    style: {},
    variant: 'text',
    color: 'default',
};

export default class Button extends Component<Props> {
    constructor(props: Props) {
        super(props);
        this.state = {
            disabled: props.disabled,
            n_clicks: props.n_clicks,
            n_clicks_previous: props.n_clicks_previous,
        };
    }

    UNSAFE_componentWillReceiveProps(nextProps: Props, nextContext: *): void {
        if (nextProps.disabled !== this.state.disabled)
            this.setState({disabled: nextProps.disabled});
    }

    handleClick() {
        const n = this.props.n_clicks + 1;
        if (this.props.setProps) this.props.setProps({n_clicks: n});
        if (this.props.setProps) this.props.setProps({n_clicks_previous: n});
        if (this.setState) this.setState({n_clicks: n});
        if (this.setState) this.setState({n_clicks_previous: n});
    }

    render() {
        const {
            className,
            classes,
            disableTouchRipple,
            disabled,
            fullWidth,
            href,
            iconClass,
            id,
            style,
            useIcon,
            disableShadow,
            variant,
            n_clicks,
            n_clicks_previous,
            color,
        } = this.props;
        let onClick;
        if (this.props.setProps) {
            onClick = this.handleClick.bind(this);
        } else {
            onClick = null;
        }
        if (!useIcon) {
            return (
                <div id={id}>
                    <ThemeProvider theme={polarcusTheme}>
                        <MUIButton
                            disableElevation={disableShadow}
                            classes={classes}
                            className={className}
                            disableTouchRipple={disableTouchRipple}
                            disabled={disabled}
                            fullWidth={fullWidth}
                            href={href}
                            style={style}
                            variant={variant}
                            onClick={onClick}
                            n_clicks={n_clicks}
                            n_clicks_previous={n_clicks_previous}
                            color={color}
                        >
                            {this.props.children}
                            <span className={iconClass} />
                        </MUIButton>
                    </ThemeProvider>
                </div>
            );
        }
        return (
            <ThemeProvider theme={polarcusTheme}>
                <div id={id}>
                    <MUIIconButton
                        classes={classes}
                        className={className}
                        disableTouchRipple={disableTouchRipple}
                        disabled={disabled}
                        href={href}
                        style={style}
                        onClick={onClick}
                        n_clicks={n_clicks}
                        n_clicks_previous={n_clicks_previous}
                    >
                        <span className={iconClass} />
                        {this.props.children}
                    </MUIIconButton>
                </div>
            </ThemeProvider>
        );
    }
}

Button.defaultProps = defaultProps;
