import React from "react"
import Link from "next/link"
import Logo from "../images/Logo.svg"


const Header = () => (
  <header className="border-gray-300 bottom-border flex items-center justify-between p-5">
   <Link href="/index" >
     <a><img src={Logo} alt="Thumbs Up News" width="250px" /></a>
   </Link>
   <nav className="flex text-xl justify-between">
     <Link href="/index"><a className="text-blue-500 pr-5">Home</a></Link>
     <Link href="/about"><a className="pr-5">About</a></Link>
     <Link href="/contacts"><a className="pr-5">Contacts</a></Link>
   </nav>
  </header>
);

export default Header
