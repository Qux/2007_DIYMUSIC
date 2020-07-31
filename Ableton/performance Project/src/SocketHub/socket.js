"use strict";

const Host_Address = "ADD YOUR HOST ADDRESS";

const Max = require("max-api");
const socket = require("socket.io-client")(Host_Address);

Max.addHandler("osc", (...args) => {
    socket.emit("osc", ...args);
});

Max.addHandler("echo", (...args) => {    
    socket.emit("echo", ...args);    
})

socket.on("connect_error", () => {
    Max.post("Connection Failed", Max.POST_LEVELS.ERROR);
    Max.outlet("connect", false);
})

socket.on("disconnect", () => {
    Max.outlet("connect", false);
})

socket.on("connect", () => {
    Max.post("Connection established.");
    Max.outlet("connect", true);

    socket.on("osc", (msg) => {        
        Max.outlet(msg);
    });

    socket.on("echo", (msg) => {                
        Max.outlet("echo", ...msg);
    })

    socket.on("info", (data) => {
        Max.outlet("info", data.connections);
    })
})

