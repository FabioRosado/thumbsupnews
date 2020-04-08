import React from "react"
import Link from "next/link"


const Footer = () => (
  <div>
    <Link href="/index"><a>Home</a></Link>
    <Link href="/about"><a>About</a></Link>
    <Link href="/contacts"><a>Contacts</a></Link>
  </div>
)

export default Footer
