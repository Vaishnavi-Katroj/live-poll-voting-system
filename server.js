const express = require("express");
const dgram = require("dgram");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const udpClient = dgram.createSocket("udp4");

const UDP_HOST = "127.0.0.1";
const UDP_PORT = 9999;

// USERS (same as your Python server)
const users = {
  Aarav: "123",
  Diya: "123",
  Rahul: "123",
  Sneha: "123",
  Kiran: "123"
};

// LOGIN
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (users[username] === password) {
    res.json({ status: "success" });
  } else {
    res.json({ status: "fail" });
  }
});

// VOTE (with UDP response handling)
app.post("/vote", (req, res) => {
  const { username, vote } = req.body;

  const message = `VOTE:${username}:${vote.toLowerCase()}`;

  udpClient.send(message, UDP_PORT, UDP_HOST);

  // Listen for response from UDP server
  udpClient.once("message", (msg) => {
    const response = msg.toString();

    if (response === "ALREADY_VOTED") {
      res.json({ status: "duplicate" });
    } else {
      res.json({ status: "accepted" });
    }
  });
});

app.listen(5000, "0.0.0.0",() => {
  console.log("🚀 Server running on all devices");
});