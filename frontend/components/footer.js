import React from "react"
import Link from "next/link"


const FooterComponent = () => (
  <footer className="border-top p-5 text-sm">  
    <nav>
      <Link href="/"><a className="nav-link mr-5">Home</a></Link>
      <Link href="/about"><a className="nav-link mr-5">About</a></Link>
      <a className="nav-link mr-5" href="https://github.com/FabioRosado/thumbsupnews">GitHub</a>
      <Link href="/contacts"><a className="nav-link mr-5">Contacts</a></Link>
      <Link href="/donate"><a className="nav-link mr-5">Donate</a></Link>
    </nav>
  </footer>  
)

export default FooterComponent
