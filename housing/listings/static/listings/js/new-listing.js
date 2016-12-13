'use strict'

$(document).ready(function(){
  $('#lease_duration_custom').hide();
  $('#furnished_details').hide();

  $("#id_lease_duration").change(function() {
    let lease_duration = $(this).val();
    if (lease_duration == "other") {
      $("#lease_duration_custom").show("fast");
    } else {
      $("#lease_duration_custom").hide("fast");
    }
  })

  $("#id_furnished").change(function() {
    let furnished = $(this).val();
    if (furnished == "lightly_furnished" || furnished == "fully_furnished") {
      $("#furnished_details").show("fast");
    } else {
      $("#furnished_details").hide("fast");
    }
  })
})
