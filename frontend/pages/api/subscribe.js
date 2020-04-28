export default async function(req, res) {

    const response = await fetch("https://api.airtable.com/v0/apps5EM1sbjCwv0Br/Newsletter", {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${process.env.AIRTABLE}`
        },
        method: "POST",
        body: req.body
    })
    return res.status(response.status).end(JSON.stringify(response))
}