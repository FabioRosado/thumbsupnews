import React, { useState } from "react"
import fetch from "isomorphic-unfetch"

import Layout from "../components/layout"
import SEO from "../components/seo"
import Main from "../components/main"


const Index = (props) =>
    <Layout>
    <SEO title="Home" />
      <Main data={props.data} />
    </Layout>

export async function getServerSideProps() {
  try {
    const res = await fetch(`${process.env.BACKEND_URL}`, {
      headers: {
        "Authorization": `Token ${process.env.TOKEN}`
      }
    })
  
    const data = await res.json()
    return {props: {data}}
  } catch(err) {
    console.log(err);
    return {props: {data: {results: [], count: 1}} }
 }
}

export default Index
