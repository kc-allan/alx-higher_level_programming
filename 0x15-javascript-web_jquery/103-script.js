$(document).ready(() => {
  function fetchTranslation (params) {
    const langCode = $('#language_code').val();
    const parameters = {
      lang: langCode
    };
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/' + '?' + $.param(parameters),
      success: (data) => {
        $('#hello').text(data.hello);
      }
    });
  }
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
