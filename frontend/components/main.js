import React, { useState, useEffect } from "react"

import { animateScroll as scroll } from "react-scroll"

import Link from "./link.js"
import Card from "./card"

const Main = (props) => {
  const [data, setData] = useState(props.data)
  const [layout, setLayout] = useState('grid-view')


  const remove_duplicated = (previous, actual) => {
    const unique = previous
    for (const article of actual) {
      if (!previous.some(existing => existing.id === article.id )) {
        unique.push(article) 
      }
    }
    return unique
  }

  const articles = url => {
    fetch('/api/get-articles', {method: 'POST', 'body': url})
      .then(results => results.json())
      .then(r => {

        if (data) {
          const unique = remove_duplicated(data.results, r.results)
          setData({next: r.next, results: unique})
        } else {
          setData(r)
        }
      })
      .catch(error => console.log(error))
  }

  const ArticlesOfSource = url => {
    fetch('/api/get-page', {method: 'POST', 'body': url})
      .then(results => results.json())
      .then(r => setData(r))
      .catch(error => console.log(error))
  }

  useEffect(() => {
    if (!data) {
      articles(process.env.BACKEND_URL)
    }

  }, [])

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
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=CNET+News`)}>CNET News</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=CNN`)}>CNN</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=Gizmodo`)}>Gizmodo</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=Life+Hacker`)}>Life Hacker</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=Mail+Online`)}>Mail Online</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=MakeUseOf`)}>MakeUseOf</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=PCWorld`)}>PCWorld</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=Sky+News`)}>Sky News</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=TechCrunch`)}>TechCrunch</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=The+Washington+Post`)}>The Washington Post</button>
                <button className="m-1 nav-link" onClick={() => ArticlesOfSource(`${process.env.BACKEND_URL}&source=Wallstreet+Journal`)}>Wallstreet Journal</button>
              </div>
            
            </div>

            <div className="flex justify-center">

              <button className="mr-3 p-3" aria-label="Change Layout to List" onClick={() => setLayout("list-view")}><i className="gg-layout-list" /></button>
              <button className="p-3" aria-label="Change Layout to Grid" onClick={() => setLayout("grid-view")}><i className="gg-layout-grid" /></button>
            
            </div>

          </div>

          {
            data ?
            <>
              <div className={layout === "grid-view" ? `main-content grid-view` : `main-content list-view`}>
                {data.results.map(article => <Card headline={article} key={article.id} />)}

                <button className="move-top" aria-label="Move To Top of Page" onClick={() => scroll.scrollToTop()}><i className="gg-chevron-up mr-1" /></button>
              </div>
              <div className="pagination flex justify-center mb-8">

              { data ? data.next ?
                <button aria-label="Load more articles flex justify-center" className="link" onClick={() => articles(data.next)}><i className="gg-arrow-down-o mr-2" /> Load More Articles...</button> :
                <button aria-label="Load more articles" className="link" onClick={() => scroll.scrollToTop()}><i className="gg-danger mr-2" /> No More Articles Available</button>
                :
                ''
              }
              
              
              </div>
            </> : <div className="flex justify-center"> <i className="gg-spinner-two mr-2" /> Loading...</div>

            
          }
        </section>
 
)}

export default Main