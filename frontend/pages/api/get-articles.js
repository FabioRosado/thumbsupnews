export default async function (req, res) {
    console.log(req.body)
    const response = await fetch(req.body, {
        headers: {
            "Authorization": `Token ${process.env.TOKEN}`
        }
    })
    const data = await response.json()

    res.status(200).json(data)
}