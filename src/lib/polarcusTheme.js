// A custom theme for this app
import {createMuiTheme} from '@material-ui/core/styles';

const theme = createMuiTheme({
    typography: {
        fontFamily: 'Lato',
        h1: {
            fontFamily: 'Amarnath',
            fontSize: 20,
        },
        h2: {
            fontFamily: 'Amarnath',
            fontSize: 14,
        },
        body1: {
            fontFamily: 'Lato',
            fontSize: 12,
        },
        body2: {
            fontFamily: 'Lato',
            fontSize: 14,
        },
        body3: {
            fontFamily: 'Lato',
            fontSize: 20,
            fontWeight: 'bold',
        },
    },
    palette: {
        primary: {
            main: '#22A637',
            light: '#E1FFE6',
            dark: '#10712C',
            A100: '#94E9A2',
        },
        secondary: {
            main: '#388681',
            light: '#80C0BD',
            dark: '#0E4A46',
        },
        error: {
            main: '#EFA79D',
            light: '#FFDAD6',
            dark: '#E66454',
        },
        info: {
            main: '#A3D979',
            light: '#DAFAC0',
            dark: '#74AD47',
        },
        warning: {
            main: '#FDD383',
            light: '#FEF0D4',
            dark: '#F5AE21',
        },
        grey: {
            one: '#4F4F4F',
            two: '#707070',
            three: '#A4A4A4',
            four: '#D2D2D2',
            five: '#E9E9E9',
            six: '#F1F1F1',
            seven: '#FBFBFB',
            white: '#FFFFFF',
        },
        background: {
            default: '#fff',
        },
        success: {
            main: '#A3D979',
            light: '#DAFAC0',
            dark: '#74AD47',
        },
    },
    overrides: {
        MuiListItem: {
            root: {
                background: 'transparent',
                '&$selected': {
                    background: 'transparent',
                },
            },
        },
        MuiButton: {
            root: {
                borderRadius: 5,
                height: 32,
                width: 150,
                fontSize: 14,
                fontWeight: 'bold',
            },
        },
        MuiToggleButton: {
            root: {
                paddingTop: 0,
                paddingBottom: 0,
                paddingLeft: 4,
                paddingRight: 4,
                height: 32,
                textTransform: 'none',
                '&$selected': {
                    backgroundColor: '#22A637',
                    color: '#fff',
                    '&:hover': {
                        backgroundColor: '#22A637',
                    },
                },
            },
        },
        MuiPaper: {
            rounded: {
                borderRadius: 10,
                // border: '0.25px solid #D2D2D2',
            },
            elevation1: {
                boxShadow: '0px 0px 2px rgba(0, 0, 0, 0.08)',
            },
            elevation2: {
                boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.08)',
            },
            elevation3: {
                boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.16)',
            },
            elevation4: {
                boxShadow: '0px 8px 16px rgba(0, 0, 0, 0.24)',
            },
        },
        MuiFormControl: {
            root: {
                width: '100%',
            },
        },
        MuiSelect: {
            root: {
                paddingLeft: 17,
                paddingTop: 8,
                paddingBottom: 8,
                fontSize: '14px',
                lineHeight: '17px',
                color: '#4F4F4F',
            },
        },
        MuiAlert: {
            outlinedError: {
                backgroundColor: '#ffdad6',
                border: '1px solid #E66454',
                color: '#707070',
                '& svg': {
                    color: '#E66454',
                },
            },
            outlinedSuccess: {
                backgroundColor: '#DAFAC0',
                border: '1px solid #74AD47',
                color: '#707070',
                '& svg': {
                    color: '#74AD47',
                },
            },
        },
        MuiOutlinedInput: {
            root: {
                fontSize: '14px',
                lineHeight: '17px',
                color: '#4F4F4F',
                marginTop: 8,
            },
            input: {
                padding: '8px !important',
            },
        },
    },
});

export default theme;
