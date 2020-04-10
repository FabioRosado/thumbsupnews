import React from "react"
import Link from "next/link"


const FooterComponent = () => (
  <footer className="border-top p-5 text-sm">  
    <nav>
      <Link href="/"><a className="nav-link mr-5">Home</a></Link>
      <Link href="/about"><a className="nav-link mr-5">About</a></Link>
      <Link href="/contacts"><a className="nav-link mr-5">Contacts</a></Link>
    </nav>
  </footer>  
)

export default FooterComponent
