import React from "react"
import Head from "next/head"

const SEO = ({title}) => (
  <Head>
    <title>{`${title} | Thumbs Up News`}</title>
    <link rel="icon" type="image/x-icon" href="icon.svg" />
  </Head>
)

export default SEO