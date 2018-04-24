# Sample code to demonstrate how the data can be diplayed in a friendly manner for non-programmers.


<head>
  <meta charset="utf-8">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.9/d3.min.js"></script>
</head>

<body>
  <script>
    
    function render(data){
      d3.select("body")
        .append("pre")
        .text(JSON.stringify(data, null, 2));
    }
    function type(d){
      d.sepal_length = +d.sepal_length;
      d.sepal_width  = +d.sepal_width;
      d.petal_length = +d.petal_length;
      d.petal_width  = +d.petal_width;
      return d;
    }
    d3.csv("iris.csv", type, render);
    
  </script>
</body>

# copy from vurran ensure to run it in visual studi
