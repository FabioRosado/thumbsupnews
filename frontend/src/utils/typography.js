import Typography from 'typography'
import gray from "gray-percentage"

const typography = new Typography({
  title: "Landl-Build",
  baseFontSize: "20px",
  baseLineHeight: 1.58,
  googleFonts: [
    {
      name: "Raleway",
      styles: ["200", "300" ,"400", "400i", "500", "700"],
    },
  ],
  headerFontFamily: ["Montserrat", "sans-serif"],
  bodyFontFamily: ["Montserrat", "sans-serif"],
  headerColor: "hsla(0,0%,0%,0.9)",
  bodyColor: "hsla(0,0%,0%,0.73)",
  headerWeight: "400",
  bodyWeight: 400,
  boldWeight: 700,
  overrideStyles: ({ adjustFontSizeTo, scale, rhythm }, options) => {
    const linkColor = "#134896"

    return {
      a: {
        color: linkColor,
        textDecoration: "underline",
      },
      "a:hover,a:active": {
        textDecoration: "none",
      },
      "h1,h2,h3,h4,h5,h6": {
        marginTop: rhythm(1.5),
        marginBottom: rhythm(0.5),
      },
      // children ol, ul
      "li>ol,li>ul": {
        marginLeft: "20px",
        marginBottom: 0,
      },
      // Blockquote styles.
      blockquote: {
        ...scale(1 / 5),
        borderLeft: `${rhythm(6 / 16)} solid ${linkColor}`,
        color: gray(35),
        paddingLeft: rhythm(10 / 16),
        fontStyle: "italic",
        marginLeft: 0,
        marginRight: 0,
      },
      "blockquote > :last-child": {
        marginBottom: 0,
      },
      "blockquote cite": {
        ...adjustFontSizeTo(options.baseFontSize),
        color: options.bodyColor,
        fontStyle: "normal",
        fontWeight: options.bodyWeight,
      },
      "blockquote cite:before": {
        content: '"— "',
      },
    }
  },
})

export default typography