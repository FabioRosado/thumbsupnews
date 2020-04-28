import React from "react"
import Layout from "../components/layout"


export default function Donate() {
  return (
    <Layout>
      <div className="my-8 mx-5 md:mx-24 md:px-24 xl:mx-64 xl:px-32">
        <h1 className="text-3xl text-center">Donate</h1>
        <p className="my-5">
          I'm building products as an learning experience and paying all 
          the expenses out of my own pocket. To keep this website running 
          it costs around 6.5 dollars a month for hosting and domain name.
        </p>

        <p className="my-5">
          If you find value on this project and would like to say thank you,
          you can pay me a coffee or two on <a className="nav-link active-link" href="https://www.buymeacoffee.com/FabioRosado">Buy Me A Coffee</a>. 
        </p>

      <p className="my-5">
        Thank you so much and hope this project keeps adding value to you!<br />FabioRosado.
      </p>
        
      </div>
    </Layout>
  );
}

