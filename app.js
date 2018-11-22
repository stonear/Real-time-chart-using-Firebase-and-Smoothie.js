var random = new TimeSeries();
$(document).ready(function() {
    var chart = new SmoothieChart({
    maxValue:10,
    minValue:-10,
    tooltip:true,
    // timestampFormatter:SmoothieChart.timeFormatter
  });
  chart.addTimeSeries(random, { strokeStyle: 'rgba(0, 255, 0, 1)', fillStyle: 'rgba(0, 255, 0, 0.2)', lineWidth: 4 });
  // delay 3 detik
  chart.streamTo(document.getElementById("chart"), 3000);

  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyA88V9rTa-pQVvKR4tJckJ7GHtNH9uEdEY",
    authDomain: "chart-b92ce.firebaseapp.com",
    databaseURL: "https://chart-b92ce.firebaseio.com",
    projectId: "chart-b92ce",
    storageBucket: "chart-b92ce.appspot.com",
    messagingSenderId: "203145862827"
  };
  firebase.initializeApp(config);

  d = $("#data");
  const dbRef = firebase.database().ref().child("data");
  dbRef.on("child_added", function(snapshot, previousChildKey) {
    // console.log(snapshot.val());
    
    // var waktu = new Date();
    // random.append(waktu.getTime(), snapshot.val().value);
    // console.log(waktu.toTimeString());

    // var waktu = new Date(snapshot.val().date + "T" + snapshot.val().time + "+07:00");
    // random.append(waktu.getTime(), snapshot.val().value);
    // console.log(waktu.toTimeString());

    var s = snapshot.val();
    JSON.parse(s).forEach(update);
  });
});

function update(value)
{
    console.log(value);
    var waktu = new Date(value.date + "T" + value.time + "+07:00");
    random.append(waktu.getTime(), value.value);
    console.log(waktu.toTimeString());
}