let pictureAmount = 8;
let totalPicture;
const src =
  'https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json';

fetch(src)
  .then(function (response) {
    return response.json();
  })
  .then((rawData) => {
    dataProceeding(rawData);
    totalPicture = rawData;
  });

function dataProceeding(data) {
  for (i = pictureAmount - 8; i < pictureAmount; i++) {
    if (i % 4 === 0) {
      let container = document.createElement('div');
      container.classList.add('content-a');
      container.setAttribute('id', 'content' + i);
      document.getElementById('center').appendChild(container);
    }
    let j = i - (i % 4);
    let containerNew = document.getElementById('content' + j);
    let n_topic = document.createElement('div');
    let n_stitle = document.createElement('div');
    let n_file = document.createElement('img');

    n_topic.appendChild(n_file);
    n_topic.appendChild(n_stitle);
    containerNew.appendChild(n_topic);

    n_topic.classList.add('box');
    n_stitle.classList.add('pic-name');
    n_file.classList.add('image');

    n_stitle.textContent = data['result']['results'][i].stitle;
    n_file.src = 'http' + data['result']['results'][i].file.split('http')[1];
  }
}

let btn = document.getElementById('btn-add');
function handler() {
  pictureAmount += 8;
  dataProceeding(totalPicture);
}

btn.addEventListener('click', handler);