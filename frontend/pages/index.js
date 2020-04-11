import React from "react"
import fetch from "isomorphic-unfetch"

import Layout from "../components/layout"


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

        <div className="flex flex-col md:flex-row p-12">
        Hello World!
        {console.log(data)}
        </div>
      </div>
    </Layout>
  );
}

Index.getInitialProps = async ctx => {
  const res = await fetch('http://localhost:8000/headlines/', {
    headers: {
      "Authorization": `Token ${process.env.TOKEN}`
    }
  })
  const json = await res.json()

  return {data: json}
}