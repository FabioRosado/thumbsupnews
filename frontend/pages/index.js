import React, { useState } from "react"
import fetch from "isomorphic-unfetch"

import Layout from "../components/layout"
import Card from "../components/card"


function Index(props) {
  const [data, setData ] = useState(props.data)
  const pages = Array.from(Array(Math.round(data.count/24)).keys());

  const category = item => {
    fetch('/api/get-category', {method: 'POST', body: item})
      .then(results => results.json())
      .then(r => setData(r))
      .catch(error => console.log(error))
  }

  const pagination = page => {
    fetch('/api/get-page', {method: 'POST', 'body': page})
      .then(results => results.json())
      .then(r => setData(r))
      .catch(error => console.log(error))
  }
  
  return (
    <Layout>
      <div className="sidebar-main">
        <div className="sidebar border-right h-screen p-8">
          <p className="sidebar-header text-sm">Categories</p>
          <ul className="my-5 side-menu text-lg">
            <li><button className="sidebar-menu-item" onClick={() => category("")}>All</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Business")}>Business</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Commodities")}>Commodities</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Entertainment")}>Entertainment</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Lifestyle")}>Lifestyle</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Markets")}>Markets</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Tech")}>Tech</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Streetwise")}>Streetwise</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Security")}>Security</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Science")}>Science</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Rumble Seat")}>Rumble Seat</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Political")}>Political</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Travel")}>Travel</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Stocks")}>Stocks</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Money")}>Money</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Health")}>Health</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Weird")}>Weird</button></li>
          </ul>
          <p className="sidebar-header text-sm ml-8">Location</p>
          <ul className="my-5 side-menu text-lg">
            <li><button className="sidebar-menu-item" onClick={() => category("World")}>World</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("US")}>US</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("UK")}>UK</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Africa")}>Africa</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("China")}>China</button></li>
            <li><button className="sidebar-menu-item" onClick={() => category("Russia")}>Russia</button></li>
          </ul>
        </div>

        <div className="main-content">
        {data.results.map(article => <Card headline={article} key={article.id} />)}
        
          <a href="#top" className="move-top"><i className="gg-chevron-up mr-1" /></a>
          <div className="pagination">
          {pages.map(page => {
              let url = ''
              if (data.next) {
                url = data.next.replace(/page=\d/gi, `page=${page+1}`)
              } 

              if (data.previous && !data.next) {
                url = data.previous.replace(/page=\d/gi, `page=${page+1}`)
              }

              return <a href="#top" key={page} className="link" onClick={() => pagination(url)}>{page+1}</a>
          })}
        </div>
        </div>
      </div>
    </Layout>
  );
}


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
    return {props: {} }
 }
}

export default Index
