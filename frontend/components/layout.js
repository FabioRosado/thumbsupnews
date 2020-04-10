import React from "react"

import Header from "./header"
import FooterComponent from "./footer"

const Layout = ({ children }) => {
  return (
    <div>
      <Header />
      <main style={{minHeight: `100vh`}}>
        {children}
     </main>
     <FooterComponent />
   </div>
  );
}

export default Layout
