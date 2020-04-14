import React from "react"
import Icon from '../images/icon.svg'

const Card = ({headline}) => (
  <article className="card">
    <header>
    <span className="letter">{headline.title.charAt(0)}</span>
      <p className="text-xs flex">
        <img src={Icon} className="mr-2" width="20px" alt={headline.categories} /> {headline.categories}
      </p>
      <h1 className="mb-5 font-semibold text-lg">{headline.title}</h1>
    </header>
    <body className="h-full">
      <p className="text-sm">{headline.description}</p>
    </body>
    <footer className="text-xs flex justify-between">
      <p className="date">{headline.date}</p>
      <p className="source">{headline.source}</p>
    </footer>
  </article>
);

export default Card