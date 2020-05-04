import React, { useState } from "react"
import Link from "./link"
import Logo from "../images/Logo.svg"


const Header = () => {
  const [show, setShow] = useState(false)
  const [hide, setHide] = useState(true)
  
  return (
    <header className="border-gray-300 border-bottom flex items-center justify-between p-5 min-w-full">
    <Link href="/" >
      <a><img src={Logo} alt="Thumbs Up News" width="250px" /></a>
    </Link>
    <button aria-label="Toggle Navigation Menu" className="visible md:invisible p-5" onClick={() => setShow(!show)}><i className="gg-menu-right" /></button>
    <nav className={show ? "navbar navbar-show" : "navbar navbar-hide"}>
      <button aria-label="Close Nagivation Menu" onClick={() => setShow(false)} className="menu-button"><i className="gg-close" /></button>
      <Link href="/"><a className="mr-5 nav-link">Home</a></Link>
      <Link href="/about"><a className="nav-link mr-5">About</a></Link>
      <a aria-label="Show Categories Available" className="nav-link nav-link-mobile cursor-pointer" onClick={() => setHide(!hide)}>Categories</a>
      <ul className={hide ? "hide pl-5" : "show pl-5"}>
        <li><Link href="/"><a className="nav-link">All</a></Link></li>
        <li><Link href="/category/art"><a className="nav-link">Art</a></Link></li>
        <li><Link href="/category/business"><a className="nav-link">Business</a></Link></li>
        <li><Link href="/category/comedy"><a className="nav-link">Comedy</a></Link></li>
        <li><Link href="/category/commodities"><a className="nav-link">Commodities</a></Link></li>
        <li><Link href="/category/education"><a className="nav-link">Education</a></Link></li>
        <li><Link href="/category/entertainment"><a className="nav-link">Entertainment</a></Link></li>
        <li><Link href="/category/environment"><a className="nav-link">Environment</a></Link></li>
        <li><Link href="/category/food"><a className="nav-link">Food</a></Link></li>
        <li><Link href="/category/health"><a className="nav-link">Health</a></Link></li>
        <li><Link href="/category/impact"><a className="nav-link">Impact</a></Link></li>
        <li><Link href="/category/lifestyle"><a className="nav-link">Lifestyle</a></Link></li>
        <li><Link href="/category/markets"><a className="nav-link">Markets</a></Link></li>
        <li><Link href="/category/money"><a className="nav-link">Money</a></Link></li>
        <li><Link href="/category/parenting"><a className="nav-link">Parenting</a></Link></li>
        <li><Link href="/category/political"><a className="nav-link">Political</a></Link></li>
        <li><Link href="/category/religion"><a className="nav-link">Religion</a></Link></li>
        <li><Link href="/category/science"><a className="nav-link">Science</a></Link></li>
        <li><Link href="/category/security"><a className="nav-link">Security</a></Link></li>
        <li><Link href="/category/stocks"><a className="nav-link">Stocks</a></Link></li>
        <li><Link href="/category/tech"><a className="nav-link">Tech</a></Link></li>
        <li><Link href="/category/travel"><a className="nav-link">Travel</a></Link></li>
        <li><Link href="/category/weird"><a className="nav-link">Weird</a></Link></li>
        <li><Link href="/category/woman"><a className="nav-link">Woman</a></Link></li>
      </ul>
      <Link href="/contacts"><a className="mr-5 nav-link">Contacts</a></Link>
      <Link href="/subscribe"><a className="primary-button">Subscribe</a></Link>
    </nav>
    </header>
)};

export default Header
