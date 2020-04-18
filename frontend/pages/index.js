import React, { useState } from "react"
import fetch from "isomorphic-unfetch"
import useSwr from 'swr'

import Layout from "../components/layout"
import Card from "../components/card"

const fetcher = url => fetch(url).then(res => res.json())


function Index(props) {
  const [data, setData ] = useState(props.data)

  const t = item => {
    fetch('/api/get-category', {method: 'POST', body: item})
      .then(results => results.json())
      .then(r => setData(r))
      .catch(error => console.log(error))
  }
  
  return (
    <Layout>
      <div className="sidebar-main">
        <div className="sidebar border-right h-screen p-8">
          <p className="sidebar-header text-sm">Categories</p>
          <ul className="my-5 side-menu text-xl">
            <li><button className="sidebar-menu-item" onClick={()=> t("")}>All</button></li>
            <li><button className="sidebar-menu-item" onClick={()=> t("Business")}>Business</button></li>
            <li><button className="sidebar-menu-item" onClick={()=> t("Lifestyle")}>Lifestyle</button></li>
            <li><button className="sidebar-menu-item" onClick={()=> t("Markets")}>Markets</button></li>
            <li><button className="sidebar-menu-item" onClick={()=> t("Tech")}>Tech</button></li>
            <li><button className="sidebar-menu-item" onClick={()=> t("Entertainment")}>Entertainment</button></li>
            <li><button className="sidebar-menu-item" onClick={()=> t("World")}>World</button></li>
          </ul>
        </div>

        <div className="main-content">
        {data.results.map(article => <Card headline={article} key={article.id} />)}
        
        </div>
      </div>
    </Layout>
  );
}


export async function getServerSideProps() {

  const moment = require('moment')
  const date = moment().format('YYYY-MM-DD')

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
    return {props: {} }
 }
}

export default Index
