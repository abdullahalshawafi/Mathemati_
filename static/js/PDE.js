var x = 0;
var parameters = {
  target: '#myFunction',
  data: [
    {
      fn: 'x * x + y * y - 2',
      fnType: 'implicit',
      color: "rgb(0,100,255)",
      interval2d: [0.5, 0.8]
    },
    {
      fn: 'x^2',
      color: "rgb(0,100,255)"
    }
  ],
  grid: true,
  yAxis: { domain: [-2, 2] },
  xAxis: { domain: [-3, 3] },
  height: window.innerWidth / 100 * 16,
  width: window.innerWidth / 100 * 23.5
};
functionPlot(parameters);

function MethodSelection() {
  var Irregular = document.getElementsByName("Method")[1];
  if (Irregular.checked) {
    document.getElementById("UXY1").style.display="none";
    document.getElementById("UXY2").style.display="none";

    document.getElementById("Dir0").style.display="none";
    document.getElementById("Dir1").style.display="none";
    document.getElementById("Dir2").style.display="none";
    document.getElementById("Dir3").style.display="none";
    document.getElementById("Dir4").style.display="none";


  } else {
    document.getElementById("UXY1").style.display="inline";
    document.getElementById("UXY2").style.display="inline";

    document.getElementById("Dir0").style.display="block";
    document.getElementById("Dir1").style.display="block";
    document.getElementById("Dir2").style.display="block";
    document.getElementById("Dir3").style.display="block";
    document.getElementById("Dir4").style.display="block";
  }
}

$(document).ready(function() {
      $('form').submit(function (e) {
          $.ajax({
              type: "POST",
              url: '/_background_process_PDE',
              data: $('form').serialize(), // serializes the form's elements.
              success: function (data) {
                if (data.error)
                {
                  alert(data.error);
                  $('#res').html(data.U);
                }
                else {
                  alert(data.U);
                  $('#res').html(data.U);
                }
              }
          });

          e.preventDefault(); // block the traditional submission of the form.
      });

      // Inject our CSRF token into our AJAX request.
      $.ajaxSetup({
          beforeSend: function(xhr, settings) {
              if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
              }
          }
      })
  });


/*

action="{{url_for('PDE')}}"
 $(function() {
       $('a#process_input').bind('click', function() {
       $.getJSON('/background_process', {
         proglang: $('input[name="proglang"]').val(),
       }, function(data) {
         $("#result").text(data.result);
       });
       return false;
       });
     });*/

var img = document.createElement("img");
img.src = "{{url_for('static', filename='Assets/Storked-Copy.svg')}}";
var src = document.getElementById("myFunction");
src.appendChild(img);
