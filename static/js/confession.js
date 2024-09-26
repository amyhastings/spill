const confessionFormBox = document.getElementById("confession-textarea");

confessionFormBox.addEventListener("input", (event) => {
    const value = confessionFormBox.value.trim();
    console.log(value);
    if (value.length < 25 || value.length > 1000)  {
        confessionFormBox.setCustomValidity("Confessions must be a minimum of 25 characters and a maximum of 1000 characters long.");
    } else if (value == null) {
        confessionFormBox.setCustomValidity("Confessions must be a minimum of 25 characters and a maximum of 1000 characters long.");
    } else {
        confessionFormBox.setCustomValidity("");
  }
});