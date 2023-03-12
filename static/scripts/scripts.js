//confirmation pops up when delete button is selected to delete a call
function confirmDelete() {
  return confirm("Are you sure you want to delete this call?");
}

//scrolls to bottom of call table
function scrollToBottom() {
  var table = document.getElementById("table");
  var lastRow = table.rows[table.rows.length -1];
  lastRow.scrollIntoView();
}

function scrollToRight() {
// Get the table element by its ID
const table = document.getElementById("table");

// Get the last cell in the last row of the table
const lastCell = table.rows[table.rows.length - 1].cells[table.rows[table.rows.length - 1].cells.length - 1];

// Calculate the offset of the last cell from the left edge of the table
const offset = lastCell.offsetLeft + lastCell.offsetWidth;

// Scroll the table to the calculated offset
table.parentElement.scrollLeft = offset;
}

function scrollToLeft() {
// Get the table element by its ID
const table = document.getElementById("table");

// Get the first cell in the first row of the table
const firstCell = table.rows[0].cells[0];

// Calculate the offset of the first cell from the left edge of the table
const offset = firstCell.offsetLeft;

// Scroll the table to the calculated offset
table.parentElement.scrollLeft = offset;
}