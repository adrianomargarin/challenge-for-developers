$(document).ready(function() {

  get_repositories = function(){
    var tag_name = $('#tag_name').val();

    $.getJSON('/repositories/?tag_name=' + tag_name, function(data){
      var template = ``;

      for(var index in data){

        var name = data[index]['name'];
        var url = data[index]['url'];
        var language = data[index]['language'];
        var tags = data[index]['tags'];

        template += `<tr>
          <td>${name}</td>
          <td>${url}</td>
          <td>${language}</td>
          <td>${tags}</td></tr>`;
      }

      $('#body-repositories').html(template);
    });
  }

  $('#search').submit(function(event){
    event.preventDefault();
    get_repositories();
  });

  get_repositories();

});
