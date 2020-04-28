import React, {useState } from "react"
import fetch from "isomorphic-unfetch"
import { useForm } from 'react-hook-form'

import Layout from "../components/layout"


export default function Subscribe() {
  const [response, setResponse] = useState(null)

  const { register, handleSubmit } = useForm()

  const onSubmit = ( data, e ) => {
    e.target.reset()
    
    fetch('/api/subscribe', {method: 'POST', body: JSON.stringify({fields: data})})
    .then(results => {
      if (results.status < 300) {
        setResponse({isError: false, message: "Subscribed to the newsletter successfully!"})
      } else {
        setResponse({isError: true, message: `An error occurred - ${results.statusText}`})
      }
    })
  }

  return (
    <Layout>
      <div className="text-center my-8 mx-5 md:mx-24 md:px-24 xl:mx-64 xl:px-32">
        <h1 className="text-3xl">Subscribe to the Newsletter</h1>
        <p className="mt-5 mb-12">You can subscribe to our weekly newsletter to get the most popular articles straight to your email!</p>
        <div className="flex flex-row md:flex-row justify-center">
            <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col">
              <label htmlFor="name" className="text-gray-500 font-semibold text-sm mb-1">Name</label>
              <input 
                name="Name"
                id="name"
                type="text"
                ref={register}
                placeholder="John Doe"
                required
                className="bg-gray-200 appearance-none contact-input w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white"
              />

              <label htmlFor="email" className="text-gray-500 font-semibold text-sm mb-1 mt-8">Email</label>
              <input 
                name="Email"
                id="email"
                type="email"
                ref={register}
                placeholder="john.doe@example.com"
                required
                className="bg-gray-200 appearance-none contact-input w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white mb-8"
              />

              <div className="flex justify-center">
                <button type="submit" className="primary-button mr-5">Submit</button>
                <button type="reset" className="primary-button">Clear</button>
              </div>
              {response && <div className={response.isError ? 
                "border-l-4 mt-8 p-2 border-red-400 bg-red-100 text-red-600 flex items-center" : 
                "border-l-4 mt-8 p-2 border-green-400 bg-green-100 text-green-600 flex items-center"}>
                <i className={response.isError ?  "gg-danger mr-2" : "gg-check-o mr-2"} /> {response.message}
              </div> }
            </form>
          </div>
        </div>
    </Layout>
  );
}
