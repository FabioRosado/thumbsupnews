import Document, { Html, Head, Main, NextScript } from 'next/document'

class ThumbsUpNews extends Document {
    static async getInitialProps(ctx) {
        const initialProps = await Document.getInitialProps(ctx)
        return { ...initialProps}
    }

    render () {
        return (
            <Html lan="en">
                <Head />
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        )
    }
}

export default ThumbsUpNews