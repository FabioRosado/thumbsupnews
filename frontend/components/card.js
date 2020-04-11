import React from "react"

const Card = ({headline}) => (
  <article className="card">
  {console.log(headline)}
    <p>{headline.categories}</p>
    <p>{headline.title}</p>
    <p>{headline.description}</p>
    <footer>
      <p>{headline.date}</p>
      <p>{headline.source}</p>
    </footer>
  </article>
);

export default Card