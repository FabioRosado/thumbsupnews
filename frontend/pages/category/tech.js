import React from 'react'

import Layout from '../../components/layout'
import Main from '../../components/main'
import fetch from 'isomorphic-unfetch'

const Tech = (props) => 
    <Layout>
      <Main data={props.data} />      
    </Layout>

export default Tech

export async function getServerSideProps() {
  try {
    const res = await fetch(`${process.env.BACKEND_URL}&search=tech`, {
    headers: {
      "Authorization": `Token ${process.env.TOKEN}`
    }
  })
  const data = await res.json()
  return {props: {data}}
} catch(err) {
    return {props: {data: {results: [], count: 1}} }
  }
}
