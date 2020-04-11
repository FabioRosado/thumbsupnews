import React from "react"
import fetch from "isomorphic-unfetch"

import Layout from "../components/layout"
import Card from "../components/card"


export default function Index({data}) {
  return (
    <Layout>
      <div className="sidebar-main">
        <div className="sidebar border-right h-screen p-8">
          <p className="sidebar-header text-sm">Categories</p>
          <ul className="my-5 side-menu text-xl font-bold">
            <li className="sidebar-menu-item active">All</li>
            <li className="sidebar-menu-item">Business</li>
            <li className="sidebar-menu-item">Lifestyle</li>
            <li className="sidebar-menu-item">Markets</li>
            <li className="sidebar-menu-item">Tech</li>
            <li className="sidebar-menu-item">Entertainment</li>
            <li className="sidebar-menu-item">World</li>
          </ul>
        </div>

        <div className="main-content">
        {data.map(article => <Card headline={article} key={article.title} />)}
        
        </div>
      </div>
    </Layout>
  );
}

Index.getInitialProps = async ctx => {
  try {
    const res = await fetch('http://localhost:8000/headlines/', {
      headers: {
        "Authorization": `Token ${process.env.TOKEN}`
      }
    })
    const json = await res.json()

    return {data: json}
  }
  catch(err) {
    console.log(err);
    return {data: []}
  }
}