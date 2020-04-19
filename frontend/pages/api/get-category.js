export default async function (req, res) {
  // We are getting the category pressed on req.body

  const response = await fetch(`${process.env.BACKEND_URL}&search=${req.body}`, {
    headers: {
      "Authorization": `Token ${process.env.TOKEN}`
    }
  })
  const data = await response.json()

    res.status(200).json(data)
}
