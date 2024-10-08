const menuButton = document.querySelector("#hamburger");
const closeMenuButton = document.querySelector("#close-menu");
const menuContainer = document.querySelector(".menu-content");


function show(item) {
    item.classList.remove("inactive");
};

function hide(item) {
    item.classList.add("inactive");
};

function openMenu() {
    show(menuContainer);
    show(closeMenuButton);
    hide(menuButton);
};

function closeMenu() {
    hide(menuContainer);
    hide(closeMenuButton);
    show(menuButton);
};

document.addEventListener('click', function(e){
    const id = e.target.id;
    if (id === "hamburger") {
        openMenu();
    } else if (id === "close-menu") {
        closeMenu();
    } 
});

// Adapted from https://www.w3schools.com/xml/xml_http.asp

function handleLike(e) {
    // Show/hide appropriate icon
    hide(e.target);
    var fields = e.target.id.split('-');
    var confession_id = fields[1];
    var unlike = document.getElementById("unlike-" + confession_id)
    show(unlike);
    // Make call to back end
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Increment counter
            var xhttp2 = new XMLHttpRequest();
            xhttp2.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                   document.getElementById("like_count-" + confession_id).innerHTML = JSON.parse(xhttp2.responseText).likes_count;
                }
            };
            xhttp2.open("GET", "/spill/" + confession_id + "/likes_count", true);
            xhttp2.send();
        }
    };
    xhttp.open("GET", "/spill/" + confession_id + "/like", true);
    xhttp.send();
}

function handleUnlike(e) {
    // Show/hide appropriate icon
    hide(e.target);
    var fields = e.target.id.split('-');
    var confession_id = fields[1];
    var like = document.getElementById("like-" + confession_id)
    show(like);
    // Make call to back end
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Decrement likes counter
            var xhttp2 = new XMLHttpRequest();
            xhttp2.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                   document.getElementById("like_count-" + confession_id).innerHTML = JSON.parse(xhttp2.responseText).likes_count;
                }
            };
            xhttp2.open("GET", "/spill/" + confession_id + "/likes_count", true);
            xhttp2.send();
        }
    };
    xhttp.open("GET", "/spill/" + confession_id + "/unlike", true);
    xhttp.send();
}

document.addEventListener('click', function(e){
    const c = e.target.classList;
    if (c.contains("like-button")) {
        handleLike(e);
    } else if (c.contains("unlike-button")) {
        handleUnlike(e);
    } 
});

