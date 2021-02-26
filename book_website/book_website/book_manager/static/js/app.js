let modes = {
  home: 0,
  add_book: 1,
  service_working: 2,
  edit_book: 3
}

let mode = modes.home
let book = {
  id: -1,
  title: '',
  author: ''
};

let authorInput = $('#author_input');
let myBooksList = $('#my_books_list');
let overlay = $('#overlay');
let overlayHeader = $('#overlay__header');
let theForm = $('form');
let titleInput = $('#title_input');



$('.add_btn').click(function() {
  setMode(modes.add_book);
})

$('#overlay__save_btn').click(function(e) {
  e.preventDefault();
  if (validateForm()) {
    if (mode === modes.add_book) {
      setMode(modes.service_working);
      fetch('/api/add_book', {
        method: 'POST',
        mode: 'same-origin',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({title: titleInput.val(), author: authorInput.val()})
      })
          .then((resp) => {
            if (resp.status === 400) {

            } else {
              return resp.json()
            }
          })
          .then((data) => {
            setMode(modes.home)
            myBooks.unshift(data[0]);
            listMyBooks();
          })
          .catch((err) => console.log(err))
    } else {
      setMode(modes.service_working);
      fetch(`/api/update_book/${book.id}`, {
        method: 'POST',
        mode: 'same-origin',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({title: titleInput.val(), author: authorInput.val()})
      })
          .then((resp) => {
            if (resp.status === 400) {

            } else {
              return resp.json()
            }
          })
          .then((data) => {
            setMode(modes.home)
            myBooks = myBooks.map((bk) => {
              console.log(bk, book)
              if (bk['pk'] === book.id) {
                return data[0]
              } else {
                return bk;
              }
            })
            listMyBooks();
          })
          .catch((err) => window.alert('unable to update book'))
    }
  }
})

$('#overlay__cancel_btn').click(function() {
  setMode(modes.home);
})

clearForm = () => {
  titleInput.val('');
  authorInput.val('');
}

deleteBook = (id) => {
  let book = extractBook(id);

  if (window.confirm(`Are you sure you want to delete ${book['fields'].title}`)) {
    myBooks = myBooks.filter((container) => container['pk'] !== id);
    listMyBooks();
    fetch(`/api/delete_book/${book['pk']}`, {
        method: 'GET',
        mode: 'same-origin',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        }
      })
          .then((resp) => {
            if (resp.status === 201) {
            } else {
              window.alert('unable to delete book')
            }
          })
          .catch((err) => {
            window.alert('unable to delete book')
          })
  }
}

editBook = (id, title, author) => {
  setMode(modes.edit_book);
  setBook({ id, title, author } );
}

extractBook = (id) => {
  return myBooks.filter((book) => book['pk'] === id)[0]
}

getCookie = (name) => {
    if (!document.cookie) {
      return null;
    }
    const token = document.cookie.split(';')
      .map(c => c.trim())
      .filter(c => c.startsWith(name + '='));

    if (token.length === 0) {
      return null;
    }
    return decodeURIComponent(token[0].split('=')[1]);
  }

listMyBooks = () => {
  myBooksList.empty();

  let listText = '';
  myBooks.forEach((container) => {
    let book = container['fields'];
    let id = container['pk'];

    listText +="<tr>\n" +
                  `<td>${book.title}</td>\n` +
                  `<td>${book.author}</td>\n` +
                  "<td>\n" +
                  `<button class=\"btn btn-sm btn-danger\" onClick='deleteBook(${ id })'>delete</button>\n` +
                  `<button class=\"btn btn-sm btn-primary edit_btn\" onClick=\"editBook(${ id }, '${ book.title }', '${ book.author }');\">edit</button>\n` +
                  " <br/>\n";

    if (book.checked_out_to)
      listText += " <span class=\"mt-2\">\n" +
                  "checked out\n" +
                  `<a class=\"btn btn-sm btn-outline-info\" href=\"/return/${ id }\">return</a>\n` +
                  "</span>\n";

    listText +=
            "</td>\n" +
            "</tr>";
  })
  myBooksList.append(listText);
}

setBook = (new_book) => {
  book = new_book;
  titleInput.val(book.title);
  authorInput.val(book.author);
}

validateForm = () => {
  let errors = [];

  if (titleInput.val().length < 3)
    errors.push('title');

  if (authorInput.val().length < 3)
    errors.push('author');

  if (errors.length) {
    for (let error in errors) {
      $(`#${errors[error]}_error`).show()
    }
  }

  return true; // errors.length === 0;
}

setMode = (new_mode) => {
  mode = new_mode;
  switch(mode) {
    case modes.add_book:
      overlay.show();
      overlayHeader.text('Add Book');
      setBook({id: -1, title: '', author: ''});
      break;
    case modes.edit_book:
      overlay.show();
      overlayHeader.text('Edit Book');
      break;
    case modes.service_working:
      overlay.show();
      overlayHeader.text('working...');
      break;
    default:
      clearForm();
      overlay.hide();
  }
}

listMyBooks();