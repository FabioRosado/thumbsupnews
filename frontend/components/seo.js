import React from "react"
import { Html } from "next/document"
import Head from "next/head"
import Icon from "../public/favicon.svg"
import Logo from "../public/thumbsupnews_white.png"

const SEO = ({title, description}) => {
  const metaDescription =  description || "Your source of positive news"
  return (
      <Head>
        <title>{`${title} | Thumbs Up News`}</title>

        <link rel="icon" type="image/svg+xm" href={Icon} />
        <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
        <link rel="manifest" href="/site.webmanifest" />
        <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5" />

        <meta httpEquiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="msapplication-TileColor" content="#da532c" />
        <meta name="theme-color" content="#ffffff" />
        <meta name="description" content={metaDescription} />
        <meta name="og:title" content={title} />
        <meta name="og:type" content="website" />
        <meta name="twitter:card" content="summary" />
        <meta name="twitter:creator" content="@FabioRosado_" />
        <meta name="twitter:title" content={`${title} | Thumbs Up News`} />
        <meta name="twitter:image:src" content={Logo} />
        <meta name="twitter:description" content={metaDescription} />

      </Head>
 )}

export default SEO
