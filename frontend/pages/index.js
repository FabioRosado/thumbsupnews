import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"
import Main from "../components/main"

const Index = (props) =>
    <Layout>
    <SEO title="Home" />
      <Main data={props.data} />
    </Layout>

export default Index