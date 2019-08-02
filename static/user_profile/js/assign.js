function store_assign(store_id, user_id){
  var s_id = parseInt(store_id, 10)
  var u_id = parseInt(user_id, 10)
  var checkBox = document.getElementById(store_id);
    if (checkBox.checked == true){
    $(document).ready(function(){
      $.ajax({ url: "/user_profile/store_assign/"+s_id+"/"+u_id+"/" })
      .done(function(res){ $('#assignments').html(res) })
    })
  } if (checkBox.checked == false){
    $(document).ready(function(){
      $.ajax({ url: "/user_profile/store_unassign/"+s_id+"/"+u_id+"/" })
      .done(function(res){ $('#assignments').html(res) })
    })
  }
}