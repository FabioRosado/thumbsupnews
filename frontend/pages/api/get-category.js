export default async function (req, res) {
  // We are getting the category pressed on req.body

  const response = await fetch(`http://localhost:8000/headlines/?sentiment=positive&categories=${req.body}`, {
    headers: {
      "Authorization": `Token ${process.env.TOKEN}`
    }
  })
  const data = await response.json()

    res.status(200).json(data)
}