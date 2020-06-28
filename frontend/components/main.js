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
        <section className="settings-panel">
          <div className="flex justify-between mt-8 px-12">
            <div className="relative mr-3 dropdown">
              <button className="ml-5 p-3 flex items-center" aria-label="Select News Source"><i className="gg-folder mr-1" />Categories</button>

              <div className="menu absolute z-10 bg-white border shadow w-64 px-8 py-4 flex-col items-start">

                <Link href="/"><a className="m-1 nav-link">All</a></Link>
                <Link href="/category/art"><a className="m-1 nav-link">Art</a></Link>
                <Link href="/category/business"><a className="m-1 nav-link">Business</a></Link>
                <Link href="/category/comedy"><a className="m-1 nav-link">Comedy</a></Link>
                <Link href="/category/education"><a className="m-1 nav-link">Education</a></Link>
                <Link href="/category/entertainment"><a className="m-1 nav-link">Entertainment</a></Link>
                <Link href="/category/environment"><a className="m-1 nav-link">Environment</a></Link>
                <Link href="/category/food"><a className="m-1 nav-link">Food</a></Link>
                <Link href="/category/health"><a className="m-1 nav-link">Health</a></Link>
                <Link href="/category/impact"><a className="m-1 nav-link">Impact</a></Link>
                <Link href="/category/lifestyle"><a className="m-1 nav-link">Lifestyle</a></Link>
                <Link href="/category/markets"><a className="m-1 nav-link">Markets</a></Link>
                <Link href="/category/parenting"><a className="m-1 nav-link">Parenting</a></Link>
                <Link href="/category/political"><a className="m-1 nav-link">Political</a></Link>
                <Link href="/category/religion"><a className="m-1 nav-link">Religion</a></Link>
                <Link href="/category/science"><a className="m-1 nav-link">Science</a></Link>
                <Link href="/category/tech"><a className="m-1 nav-link">Tech</a></Link>
                <Link href="/category/travel"><a className="m-1 nav-link">Travel</a></Link>
                <Link href="/category/weird"><a className="m-1 nav-link">Weird</a></Link>
                <Link href="/category/woman"><a className="m-1 nav-link">Woman</a></Link>
            </div>
          
          </div>
            <div className="relative mr-3 dropdown">
              <button className="p-3 flex items-center" aria-label="Select News Source"><i className="gg-website mr-1" />Source</button>

              <div className="menu absolute z-10 bg-white border shadow w-64 px-8 py-4 flex-col items-start">
                <button className="m-1 nav-link">CNET News</button>
                <button className="m-1 nav-link">Mail Online</button>
                <button className="m-1 nav-link">CNN</button>
                <button className="m-1 nav-link">Sky News</button>
                <button className="m-1 nav-link">Life Hacker</button>
                <button className="m-1 nav-link">MakeUseOf</button>
                <button className="m-1 nav-link">TechCrunch</button>
                <button className="m-1 nav-link">The Washington Post</button>
                <button className="m-1 nav-link">PCWorld</button>
                <button className="m-1 nav-link">Wallstreet Journal</button>
                <button className="m-1 nav-link">Gizmodo</button>
              </div>
            
            </div>

            <div className="flex justify-center">

              <button className="mr-3 p-3" aria-label="Change Layout to List" onClick={() => setLayout("list-view")}><i className="gg-layout-list" /></button>
              <button className="p-3" aria-label="Change Layout to Grid" onClick={() => setLayout("grid-view")}><i className="gg-layout-grid" /></button>
            
            </div>

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
 
)}

export default Main
