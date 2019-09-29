var map, address;

function initMap() {
    var geocoder = new google.maps.Geocoder;
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            geocodeLatLng(geocoder, pos.lat, pos.lng);
            // document.getElementById('calculatedData').style.display = "initial";
            document.getElementById('calculatedData').style.visibility = "visible";

            //calcRoute();
        });
    } 
}


function geocodeLatLng(geocoder,lati,long) {
        var latlng = {lat: parseFloat(lati), lng: parseFloat(long)};
        geocoder.geocode({'location': latlng}, function(results, status) {
          if (status === 'OK') {
            if (results[0]) {
              var marker = new google.maps.Marker({
                position: latlng,
              });
                address = results[0].formatted_address;
                windows.alert(address);
                var field = document.getElementById('formLocation');
                field.value =address;
                
            } else {
              window.alert('No results found');
            }
          } else {
            window.alert('Geocoder failed due to: ' + status);
          }
        });
    }
    // var destination= ['','','','',''];

// function calcRoute() {
//     // var start = document.getElementById('start').value;
//     // var end = d ocument.getElementById('end').value;
//     var request = {
//         origin: address,
//         destination: 'Trillium Health Partners - Credit Valley Hospital',
//         travelMode: 'DRIVING'
    // };
    
    //document.getElementById('end').innerHTML = request.destination;
    //destination[0]= request.destination;
    //destination[1]= request.destination;
    //destination[2]= request.destination;

    // https://www.google.com/maps/search/?api=1&query=centurylink+field
    // str1.concat(str2);

    

    // directionsService.route(request, function (response, status) {
    //     if (status == 'OK') {
    //         directionsRenderer.setDirections(response);
    //     }
    // });
// }