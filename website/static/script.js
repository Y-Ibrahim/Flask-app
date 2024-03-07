// select all filter buttons and filterable cards
const filterButtons = document.querySelectorAll("#filter-buttons button")
const filterableCards = document.querySelectorAll("#filter-cards .card")

const filterCards = (e) => {
    document.querySelector(".active").classList.remove("active");
    e.target.classList.add("active");
    console.log(e.target.dataset.name)

    // Iterate over each card
    filterableCards.forEach(card => {
        // Add "hide" class to hide card initially
        // console.log(card.dataset.name)
        // Check if the card matches the selected filter or "all" is selected
        if(card.dataset.name === e.target.dataset.name || e.target.dataset.name === "all"){
            return card.classList.replace("hide", "show");   
        }
        card.classList.add("hide");
    })
}


// add click event listener for each filter button
filterButtons.forEach(button => button.addEventListener("click", filterCards));



// Popup 

// Get the popup and button elements
var popup = document.getElementById("postCardForm");
var openBtn = document.getElementById("openFormBtn");

// Get the close button element
var closeBtn = document.getElementsByClassName("close")[0];

// When the user clicks the button, display the popup
openBtn.onclick = function() {
    popup.style.display = "block";
}

// When the user clicks on the close button, hide the popup
closeBtn.onclick = function() {
    popup.style.display = "none";
}

// When the user clicks anywhere outside of the popup, close it
window.onclick = function(event) {
    if (event.target == popup) {
        popup.style.display = "none";
    }
}


// close form when "close-btn" is pressed
function openForm() {
  document.getElementById("formOverlay").style.display = "block";
}

function closeForm() {
        document.getElementById("formOverlay").style.display = "none";
    }