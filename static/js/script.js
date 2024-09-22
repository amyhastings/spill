
function show(item) {
    item.classList.remove("inactive");
};

function hide(item) {
    item.classList.add("inactive");
};

// Adapted from https://www.w3schools.com/xml/xml_http.asp

function handleLike(e) {
    // show/hide
    hide(e.target);
    var fields = e.target.id.split('-');
    var confession_id = fields[1];
    var unlike = document.getElementById("unlike-" + confession_id)
    show(unlike);
    // make call to back end
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // increment counter
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
    // show/hide
    hide(e.target);
    var fields = e.target.id.split('-');
    var confession_id = fields[1];
    var like = document.getElementById("like-" + confession_id)
    show(like);
    // make call to back end
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // increment counter
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
    //e.preventDefault();
    if (c.contains("like-button")) {
        handleLike(e);
    } else if (c.contains("unlike-button")) {
        handleUnlike(e);
    } 
});

