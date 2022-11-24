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