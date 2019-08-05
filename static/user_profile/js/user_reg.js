$(document).ready(function(){
  $('#fname').keyup(function(){
    var data = $("#regForm").serialize() 
    $.ajax({
      method: "POST",
      url: "/user_profile/fname/",
      data: data
    })
    .done(function(res){
      $('#fnameMsg').html(res)
    })
  })
})

$(document).ready(function(){
  $('#lname').keyup(function(){
    var data = $("#regForm").serialize() 
    $.ajax({
      method: "POST", 
      url: "/user_profile/lname/",
      data: data
    })
    .done(function(res){
      $('#lnameMsg').html(res)
    })
  })
})

$(document).ready(function(){
  $('#em').keyup(function(){
    var data = $("#regForm").serialize() 
    $.ajax({
      method: "POST", 
      url: "/user_profile/email/",
      data: data
    })
    .done(function(res){
      $('#emailMsg').html(res) 
    })
  })
})

$(document).ready(function(){
  $('#pw').keyup(function(){
    var data = $("#regForm").serialize() 
    $.ajax({
      method: "POST",
      url: "/user_profile/pword/",
      data: data
    })
    .done(function(res){
      $('#pwordMsg').html(res)
    })
  })
})

$(document).ready(function(){
  $('#cpw').keyup(function(){
    var data = $("#regForm").serialize() 
    $.ajax({
      method: "POST",
      url: "/user_profile/c_pword/",
      data: data
    })
    .done(function(res){
      $('#c_pwordMsg').html(res) 
    })
  })
})


$(document).ready(function(){
  $('#dob').change(function(){
    
      var data = $("#regForm").serialize() 
      $.ajax({
        method: "POST", 
        url: "/user_profile/dob/",
        data: data
      })
      .done(function(res){
        $('#dobMsg').html(res) 
      })
    
  })
})

