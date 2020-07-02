const fetch = require("node-fetch")

export default async function (req, res) {
    const data = JSON.parse(req.body)

    const response = await fetch(`${process.env.BACKEND_ROOT_URL}/headlines/${data.id}`, {
        headers: {
            "Authorization": `Token ${process.env.TOKEN}`,
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=UTF-8'
        },
        method: "PUT",
        body: req.body
    })
    return res.status(response.status).end(response.statusText)
    
}
