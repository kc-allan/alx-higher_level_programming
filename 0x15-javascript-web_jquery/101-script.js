document.addEventListener('DOMContentLoaded', () => {
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(() => {
    $('.my_list li:eq(-1)').remove();
  });
  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});
