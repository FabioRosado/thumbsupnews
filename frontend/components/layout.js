import React from "react"

import Header from "./header"
import FooterComponent from "./footer"

const Layout = ({ children }) => {
  return (
    <>
      <Header />
      <main style={{minHeight: `100vh`}}>
        {children}
     </main>
     <FooterComponent />
   </>
  );
}

export default Layout
