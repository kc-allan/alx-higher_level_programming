$(document).ready(() => {
  $('#btn_translate').click(() => {
    const lang_code = $('#language_code').val();
    const params = {
      lang: lang_code
    };
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/' + '?' + $.param(params),
      success: (data, statusCode) => {
        if (statusCode === 'success') {
          $('#hello').text(data.hello);
        }
      }
    });
  });
});
