const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data, status) {
  if (status === 'success') {
    $('#hello').text(data.hello);
  }
});
