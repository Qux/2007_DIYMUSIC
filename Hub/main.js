'use strict';

const Listen_Port = "SET PORT";

const io = require("socket.io").listen(Listen_Port);
//const server = io.listen(Listen_Port);


const broadcastInfo = () => {
    const data = {
        "connections": io.engine.clientsCount
    };
    io.emit("info", data);
}

io.on("connection", (socket) => {
    console.log("a user connected");
    broadcastInfo();

    socket.on("osc", (...msg) => {
        console.log("Message received: ", msg);
        socket.broadcast.emit("osc", msg);
    });

    socket.on("echo", (...msg) => {
        console.log("echo", msg);    
        io.to(socket.id).emit("echo", msg);
    });

    socket.on('disconnect', () => {
        broadcastInfo();
    })
});

