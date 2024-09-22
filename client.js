"use strict";
var socket = io();

// Map a numeric value to a color gradient
function mapValueToColor(value) {
    if (value < 25) {
        return "white";
    } else if (value < 50) {
        return "green";
    } else if (value < 75) {
        return "yellow";
    } else if (value < 100) {
        return "orange";
    } else {
        return "red";
    }
}

// Read the data from the MQTT message that the server sent and 
// display it on the webpage with a color gradient
socket.on('mqtt_message', function(msg) {
    var value = parseFloat(msg.payload);  // Parse the payload as a floating-point number
    document.getElementById("variabletext").innerHTML = value;  // Display the value
    console.log('msg:', msg);

    // Map the value to a color and set the text color accordingly
    var textColor = mapValueToColor(value);
    document.getElementById("variabletext").style.color = textColor;
});
