import React from "react"
import fetch from 'isomorphic-unfetch'


const Card = ({headline}) => {
  const description = headline.description.substring(0, 250)

  const colors = ['gray', 'pink', 'green', 'blue']
  const random = Math.floor(Math.random() * colors.length)

  const addClick = (data) => {
    data.clicks++
    fetch('/api/update-article', {method: "POST", body: JSON.stringify(data)})
  }


  return (      
    <article className={`card card-${colors[random]}`}>
      <header>
      <a href={headline.link} onClick={() => addClick(headline)}>
      <span className="letter">{headline.title.charAt(0)}</span>
        <p className="text-xs flex">
         {headline.categories}
        </p>
        <h1 className="mb-5 font-semibold text-lg">{headline.title}</h1>
      </a>
      </header>
      <div className="h-full">
        <a href={headline.link} onClick={() => addClick(headline)}>
        <p className="text-sm">{description.replace(/\W$/, '')}... | Read More</p>
        </a>
      </div>
      <footer className="text-xs flex justify-between mt-3">
        <p className="date">{headline.date}</p>
        <p className="source">{headline.source}</p>
      </footer>
    </article>
  )};

export default Card
