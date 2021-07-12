import express from "express";
import bodyParser from "body-parser";
const fs = require("fs");
import cors from "cors";
const apiData = require("../../data.json");

const app = express();
const { PORT = 3000 } = process.env;

app.use(bodyParser.json());

app.get("", (request, response) => response.send("Hello World"));

app.get("/members", (request, response) => {
    let members = apiData.data.members;
    response.json(members).status(200);
});

app.post("/members", (req, res) => {
    const members = apiData.data.members;
    const id = members.length + 1;

    const body = {
        id,
        ...req.body
    };

    apiData.data.members.push(body);
    const data = JSON.stringify(apiData, null, 4);

    fs.writeFileSync("../../data.json", data, err => {

        // Check for error
        if (err) throw err;

        // Success
        console.log("Done writing");
    });

    res.json(body).status(200)
});

app.get("/members/:id", (req, res) => {
    let id = parseInt(req.params.id);
    let members = apiData.data.members;
    let response = members.find(member => member.id === id);
    if (!response) {
        res.status(404).json({ message: `Member with ID: ${id} doesn't exist` });
    }
    res.json(response).status(200);
});



app.listen(PORT, () =>
    console.log(`Hello World, I'm listening on port ${PORT}!`)
);