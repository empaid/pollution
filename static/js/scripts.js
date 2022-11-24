$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=addcity_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var $success = $form.find(".success");
  var data = $form.serialize();

  $.ajax({
    url: "/user/addcity",
    type: "GET",
    data: data,
    dataType: "json",
    success: function(resp) {
      $success.text("City Added Successfully").removeClass("error--hidden");
      $error.addClass("error--hidden");
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
      $success.addClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=removecity_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var $success = $form.find(".success");
  var data = $form.serialize();

  $.ajax({
    url: "/user/removecity",
    type: "GET",
    data: data,
    dataType: "json",
    success: function(resp) {
      $success.text("City Removed Successfully").removeClass("error--hidden");
      $error.addClass("error--hidden");
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
      $success.addClass("error--hidden");
    }
  });

  e.preventDefault();
});
var getLocation = function(href) {
  var l = document.createElement("a");
  l.href = href;
  return l;
};
const params = new Proxy(new URLSearchParams(window.location.search), {
  get: (searchParams, prop) => searchParams.get(prop),
});
let city = params.city; 
$(document).ready(async function(){
    var l = getLocation(window.location.search);
    if(l.pathname.includes("static/cityanalytics")){
    response = await fetch('/user/cities') 
    cities = await response.json();
    console.log(cities)
    cities.forEach(city => $("#citylist").append(`<li><a class="dropdown-item" href="cityanalytics.html?city=`+city+`">`+city.toUpperCase()+`</a></li>`));
    if(city){
      $('.page-title').text('Analytics over Time for '+city.toUpperCase());
    }
    else{
      $('.page-title').text('Select City from Below Drop Down');
    }
  } 
   
});