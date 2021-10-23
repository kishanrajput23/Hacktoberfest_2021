
window.onload=  () =>{
    const form1 = document.querySelector('#addForm');

    let items = document.getElementById('items');
    let submit = document.getElementById('submit');

    let editItem = null;

    form1.addEventListener('submit', addItem);
    items.addEventListener('click', removeItem);
}

function addItem(e) {
      e.preventDefault();
    if(submit.value != 'ADD'){
        let y=editItem.target.parentNode.childNodes[0];
         y.childNodes[0].textContent= document.getElementById('item').value;
         y.childNodes[2].textContent= document.getElementById('comment2').value;
         y.childNodes[1].textContent="";
         y.childNodes[3].textContent="";
        var i;
        for (i = 0; i < document.getElementById('comment3').value; i++) {
          let c=document.createElement('i');
          c.className = "far fa-star";
          y.childNodes[1].appendChild(c);
      }
      var today = new Date();

      var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();

      var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

      var dateTime = date+' '+time;
      y.childNodes[3].appendChild(document.createTextNode(dateTime));
        submit.value = "ADD";

        document.getElementById("lblsuccess").innerHTML = "Text edited successfully";
        document.getElementById("lblsuccess").style.display = "block";
        setTimeout( function(){ document.getElementById("lblsuccess").style.display = "none"; } ,3000);

        document.getElementById('item').value = '';
        document.getElementById('comment2').value = '';
        document.getElementById('comment3').value = '';

        return false;
    }

    let newItem = document.getElementById('item').value;
    let newItem1 = document.getElementById('comment2').value;
    let newItem2 = document.getElementById('comment3').value;
    if(newItem.trim() == '' || newItem.trim() ==null){
        return false;
    }else{
        document.getElementById('item').value = '';
        document.getElementById('comment2').value = '';
        document.getElementById('comment3').value = '';
    }
    let li = document.createElement('li');
    li.className = "card";

    let deleteButton = document.createElement('button');
    deleteButton.className = "btn-danger btn btn-sm float-right delete";

    deleteButton.appendChild(document.createTextNode("Delete"));

    let editButton = document.createElement('button');
    editButton.className = "btn-success btn btn-sm float-right edit";

    editButton.appendChild(document.createTextNode("Edit"));
    let card=document.createElement('div');
    card.className = "card-body";
    let cardtitle=document.createElement('h4');
    cardtitle.className = "card-title";
    cardtitle.appendChild(document.createTextNode(newItem));
    let cardsubtitle=document.createElement('h6');
    cardsubtitle.className = "card-subtitle";
    var i;
    for (i = 0; i < newItem2; i++) {
      let c=document.createElement('i');
      c.className = "far fa-star";
      cardsubtitle.appendChild(c);
  }
  let cardtext=document.createElement('p');
  cardtext.className = "card-text d-none d-md-block";
  cardtext.appendChild(document.createTextNode(newItem1));
  let carddate=document.createElement('p');
  carddate.className = "card-text text-muted";
  var today = new Date();

  var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();

  var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

  var dateTime = date+' '+time;
  carddate.appendChild(document.createTextNode(dateTime));
    card.appendChild(cardtitle);
    card.appendChild(cardsubtitle);
    card.appendChild(cardtext);
    card.appendChild(carddate);
    li.appendChild(card);
    li.appendChild(deleteButton);
    li.appendChild(editButton);

    items.appendChild(li);
}

function removeItem(e){

    e.preventDefault();
    if(e.target.classList.contains('delete')){
        if(confirm("Are you Sure?")){
            let li = e.target.parentNode;
            items.removeChild(li);
            document.getElementById("lblsuccess").innerHTML = "Text deleted successfully";
            document.getElementById("lblsuccess").style.display = "block";
            setTimeout( function(){ document.getElementById("lblsuccess").style.display = "none"; } ,3000);
        }
    }
    if(e.target.classList.contains('edit')){
        let y=e.target.parentNode.childNodes[0];
        document.getElementById('item').value = y.childNodes[0].textContent;
        document.getElementById('comment2').value = y.childNodes[2].textContent;
        document.getElementById('comment3').value = "";
        submit.value = "EDIT";
        editItem = e;
    }
}

function toggleButton(ref,btnID){
    document.getElementById(btnID).disabled = false;
}
