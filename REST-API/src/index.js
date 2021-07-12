import express from "express";
import bodyParser from "body-parser";
const fs = require("fs");
import cors from "cors";
const apiData = require("../../data.json");

const app = express();
const { PORT = 3000 } = process.env;

app.use(bodyParser.json());

app.get("", (request, response) => response.send("FTWin's REST API"));

// Request to get array of all members.
app.get("/members", (request, response) => {
    let members = apiData.data.members;
    response.json(members).status(200);
});

// Post for adding a new member.
app.post("/members", (req, res) => {
    const members = apiData.data.members;
    const id = members.length + 1;

    const body = {
        id,
        ...req.body
    };

    apiData.data.members.push(body);
    const data = JSON.stringify(apiData, null, 4);

    fs.writeFileSync("../data.json", data, err => {

        // Check for error
        if (err) throw err;

        // Success
        console.log("Done writing");
    });

    res.json(body).status(200)
});

// Request to get a specific member by id.
app.get("/members/:id", (req, res) => {
    let id = parseInt(req.params.id);
    let members = apiData.data.members;
    let response = members.find(member => member.id === id);
    if (!response) {
        res.status(404).json({ message: `Member with ID: ${id} doesn't exist` });
    }
    res.json(response).status(200);
});

// Request to get a specific member by name
app.get("/members/name/:name", (req, res) => {
    let name = req.params.name;
    let members = apiData.data.members;
    let response = members.find(member => member.name === name);
    if (!response) {
        res.status(404).json({ message: `Member with name: ${name} doesn't exist` });
    }
    res.json(response).status(200);
});

// Request a specific member's current weapons by id
app.get("/members/:id/current_weapons", (req, res) => {
    let id = parseInt(req.params.id);
    let members = apiData.data.members;
    let response = members.find(member => member.id === id);
    if (!response) {
        res.status(404).json({ message: `Member with ID: ${id} doesn't exist` });
    }
    res.json(response.current_weapons).status(200);
});

// Request a specific member's weapon history by id
app.get("/members/:id/weapon_history", (req, res) => {
    let id = parseInt(req.params.id);
    let members = apiData.data.members;
    let response = members.find(member => member.id === id);
    if (!response) {
        res.status(404).json({ message: `Member with ID: ${id} doesn't exist` });
    }
    res.json(response.weapon_history).status(200);
});

// Request a specific member's social media by id
app.get("/members/:id/social_media", (req, res) => {
    let id = parseInt(req.params.id);
    let members = apiData.data.members;
    let response = members.find(member => member.id === id);
    if (!response) {
        res.status(404).json({ message: `Member with ID: ${id} doesn't exist` });
    }
    res.json(response.social_media).status(200);
});

// Request a specific member's biography by id
app.get("/members/:id/biography", (req, res) => {
    let id = parseInt(req.params.id);
    let members = apiData.data.members;
    let response = members.find(member => member.id === id);
    if (!response) {
        res.status(404).json({ message: `Member with ID: ${id} doesn't exist` });
    }
    res.json(response.biography).status(200);
});

app.listen(PORT, () =>
    console.log(`Hello World, I'm listening on port ${PORT}!`)
);