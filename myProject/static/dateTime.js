var d = new Date();
var monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
];

var date = document.getElementById("date");

// var time = document.getElementById("time");

function getDate() {
    date.innerHTML =
        monthNames[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear();
}

getDate();

