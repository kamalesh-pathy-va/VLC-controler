const express = require("express");

const app = express();
console.log("Running server.");
app.listen(4382, () => console.log("Port: 4382"));
app.use(express.static("public"));
app.use(express.json({ limit: '1mb' }));

var currentLog;

app.post('/api', (request, response) => {
    const incomingData = request.body;
    currentLog = incomingData;
    console.log(incomingData);
    response.json(incomingData);
});

app.get('/api', (request, response) => {
    response.json(currentLog);
});