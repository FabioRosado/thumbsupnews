
export default async function (req, res) {
    const data = JSON.parse(req.body)
    if (!data.lastName) {
        const response = await fetch(`${process.env.BACKEND_ROOT_URL}/contact/`, {
            headers: {
                "Authorization": `Token ${process.env.TOKEN}`,
                'Content-Type': 'application/json' 
            },
            method: "POST",
            body: req.body
        })
        return res.status(response.status).end(response.statusText)
    }
}