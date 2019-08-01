

$(document).ready(function(){
  $('#send').click(function(){
    var message = $("#message_form").serialize() // capture all the data in the form in the variable data
    var ticket = document.getElementById('ticket_id').value;
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "/service/create_message/"+ticket+"/",
      data: message
    })
    .done(function(res){
      $('#messages').html(res) // manipulate the dom when the response comes back
      document.getElementById('message').value = "";
    })
  })
})

function delete_message(msg_id){

  $(document).ready(function(){
      
      $.ajax({
        // method: "POST", // we are using a post request here, but this could also be done with a get
        url: "/service/delete_message/"+msg_id+"/",
        // data: message_to_delete_form
      })
      .done(function(res){
        $('#messages').html(res) // manipulate the dom when the response comes back
      })
    
  })
}
