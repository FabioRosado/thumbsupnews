import React, { useState } from "react"
import { animateScroll as scroll } from "react-scroll"

import Link from "./link.js"
import Card from "./card"

const Main = (props) => {
  const [data, setData] = useState(props.data)
  const pages = Array.from(Array(Math.round(data.count/24)).keys())

  const [layout, setLayout] = useState('grid-view')


  const pagination = page => {
    fetch('/api/get-page', {method: 'POST', 'body': page})
      .then(results => results.json())
      .then(r => {
        setData(r) 
        scroll.scrollToTop()})
      .catch(error => console.log(error))
  }

  return (
     <div className="sidebar-main">
        <div className="sidebar border-right h-screen p-8">
          <p className="sidebar-header text-sm">Categories</p>
          <ul className="my-5 side-menu text-lg">
            <li><Link href="/"><a className="sidebar-menu-item">All</a></Link></li>
            <li><Link href="/category/art"><a className="sidebar-menu-item">Art</a></Link></li>
            <li><Link href="/category/business"><a className="sidebar-menu-item">Business</a></Link></li>
            <li><Link href="/category/comedy"><a className="sidebar-menu-item">Comedy</a></Link></li>
            <li><Link href="/category/education"><a className="sidebar-menu-item">Education</a></Link></li>
            <li><Link href="/category/entertainment"><a className="sidebar-menu-item">Entertainment</a></Link></li>
            <li><Link href="/category/environment"><a className="sidebar-menu-item">Environment</a></Link></li>
            <li><Link href="/category/food"><a className="sidebar-menu-item">Food</a></Link></li>
            <li><Link href="/category/health"><a className="sidebar-menu-item">Health</a></Link></li>
            <li><Link href="/category/impact"><a className="sidebar-menu-item">Impact</a></Link></li>
            <li><Link href="/category/lifestyle"><a className="sidebar-menu-item">Lifestyle</a></Link></li>
            <li><Link href="/category/markets"><a className="sidebar-menu-item">Markets</a></Link></li>
            <li><Link href="/category/parenting"><a className="sidebar-menu-item">Parenting</a></Link></li>
            <li><Link href="/category/political"><a className="sidebar-menu-item">Political</a></Link></li>
            <li><Link href="/category/religion"><a className="sidebar-menu-item">Religion</a></Link></li>
            <li><Link href="/category/science"><a className="sidebar-menu-item">Science</a></Link></li>
            <li><Link href="/category/tech"><a className="sidebar-menu-item">Tech</a></Link></li>
            <li><Link href="/category/travel"><a className="sidebar-menu-item">Travel</a></Link></li>
            <li><Link href="/category/weird"><a className="sidebar-menu-item">Weird</a></Link></li>
            <li><Link href="/category/woman"><a className="sidebar-menu-item">Woman</a></Link></li>
          </ul>
        </div>
        <section>
          <div className="flex justify-end mt-8 mb-2 pr-12">
          <button className="mr-6" aria-label="Change Layout to List" onClick={() => setLayout("list-view")}><i className="text-gray-700 gg-layout-list" /></button>
          <button className="" aria-label="Change Layout to Grid" onClick={() => setLayout("grid-view")}><i className="text-gray-700 gg-layout-grid" /></button>
          </div>

          <div className={layout === "grid-view" ? `main-content grid-view` : `main-content list-view`}>
          {data.results.map(article => <Card headline={article} key={article.id} />)}
            <button className="move-top" aria-label="Move To Top of Page" onClick={() => scroll.scrollToTop()}><i className="gg-chevron-up mr-1" /></button>
          </div>
          <div className="pagination flex justify-center mb-8">
            {pages.map(page => {
                let url = ''
                if (data.next) {
                  url = data.next.replace(/page=\d/gi, `page=${page+1}`)
                } 

                if (data.previous && !data.next) {
                  url = data.previous.replace(/page=\d/gi, `page=${page+1}`)
                }
                return <button key={page} aria-label={`Move to page ${page+1}, will scroll to top`} className="link" onClick={() => pagination(url)}>{page+1}</button>
            })}
          </div>
        
        </section>
      </div>
 
)}

export default Main
