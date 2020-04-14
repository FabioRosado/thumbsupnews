import React from "react"
import Link from "./link"
import Logo from "../images/Logo.svg"


const Header = () => (
  <header className="border-gray-300 border-bottom flex items-center justify-between p-5 min-w-full">
   <Link href="/" >
     <a><img src={Logo} alt="Thumbs Up News" width="250px" /></a>
   </Link>
   <nav className="flex items-center">
     <Link href="/"><a className="mr-5 nav-link">Home</a></Link>
     <Link href="/about"><a className="mr-5 nav-link">About</a></Link>
     <Link href="/contacts"><a className="mr-5 nav-link">Contacts</a></Link>
     <Link href="/subscribe"><a className="primary-button">Subscribe</a></Link>
   </nav>
  </header>
);

export default Header
