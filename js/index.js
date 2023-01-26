document.getElementById("search").addEventListener("keyup", cardFilter);
document.getElementById("title").addEventListener("click", () => {
  location.href = "https://github.com/minyong-jeong/python-cheatsheet";
});

window.onload = () => {
  document.getElementById("search").value = "";
  createCard();
};

function cardFilter() {
  const cards = document.getElementById("cards");
  const card = cards.getElementsByClassName("card");

  let filter, txtValue;
  filter = document.getElementById("search").value.toUpperCase();

  for (let i = 0; i < card.length; i++) {
    txtValue = card[i].innerText;
    txt_ok = txtValue.toUpperCase().indexOf(filter) > -1;
    card[i].style.display = (txt_ok) ? "" : "none";
  }
}

function createCard() {
  let cards = '';
  for (const key in PYTHON_LIST) {
    cards = cards + `<a href="${PYTHON_LIST[key]}" class="card"><h3>${key}</h3></a>`;
  }
  document.getElementById("cards").innerHTML = cards;
}
