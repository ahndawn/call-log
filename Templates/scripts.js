
//confirmation pops up when delete button is selected to delete a call
function confirmDelete() {
    return confirm("Are you sure you want to delete this call?");
}


//auto-populates appropriate area to community
const communitySelect = document.querySelector('#community-select');
const areaSelect = document.querySelector('#area-select');
    
communitySelect.addEventListener('change', (event) => {
    const community = event.target.value;
    if (community === 'hunters_run') {
        areaSelect.value = 'north';
    } else if (community === 'valencia_cove') {
        areaSelect.value = 'central';
    } else if (community === 'ibis') {
        areaSelect.value = 'west';
    }
});


//formats phone number in 'phone_number input' in calls.html table
function formatPhoneNumber() {
    const phoneNumber = document.getElementById('phone_number');
    const cleanedPhoneNumber = phoneNumber.value.replace(/\D/g, '');
  
    if (cleanedPhoneNumber.length === 10) {
      const formattedPhoneNumber = `(${cleanedPhoneNumber.slice(0, 3)}) ${cleanedPhoneNumber.slice(3, 6)}-${cleanedPhoneNumber.slice(6)}`;
      phoneNumber.value = formattedPhoneNumber;
    }
  }

// scrolls to bottom of call table
  function scrollToBottom() {
    var table = document.getElementById("table");
    var lastRow = table.rows[table.rows.length -1];
    lastRow.scrollIntoView({behavior: 'smooth'});
}
