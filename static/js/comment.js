const commentFormBox = document.getElementById("spill-comment");

commentFormBox.addEventListener("input", (event) => {
    const value = commentFormBox.value.trim();
    console.log(value.length)
    if (value.length < 2 || value.length > 1000)  {
        commentFormBox.setCustomValidity("Comments must be a minimum of 1 character and a maximum of 500 characters long.");
    } else {
        commentFormBox.setCustomValidity("");
  }
});