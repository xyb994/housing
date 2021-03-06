'use strict'

$(document).ready(function(){
  if ($('#id_furnished').val() == 'lightly_furnished' || $('#id_lease_duration').val() == 'fully_furnished') {
    $('#furnished_details').show('fast');
  }

  if ($('#id_lease_duration').val() != 'other') {
    $('#lease_duration_custom').hide('fast');
  }

  $('#id_lease_duration').change(function() {
    let lease_duration = $(this).val();
    if (lease_duration == 'other') {
      $('#lease_duration_custom').show('fast');
    } else {
      $('#lease_duration_custom').hide('fast');
      $('#id_lease_duration_custom').val("");
    }
  })

  $('#id_furnished').change(function() {
    let furnished = $(this).val();
    if (furnished == 'lightly_furnished' || furnished == 'fully_furnished') {
      $('#furnished_details').show('fast');
    } else {
      $('#furnished_details').hide('fast');
      $('#id_furnished_details').val("");
    }
  })
})
