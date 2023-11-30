MY_KEY = 'https://api.weatherapi.com/v1/current.json?q=london';


// FETCHING DATA
// URL (required), options (optional)
fetch('https://url.com/some/url',{mode: 'cors'}) // cors in case some website restricts our access
  .then(function(response) {
    return response.json();
  })
  .catch(function(response) {
    console.log(response);
  });