#make a new index.html file

texto="""<!DOCTYPE HTML>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="author"      content="">
    <meta name="description" content="">
    <meta name="keywords"    content="">
    <meta name="viewport"    content="width=device-width, initial-scale=1">
    <title>    </title>
    <!-- Bootstrap CSS --> 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <!-- icons Bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
  </head>

  <body>

    <!-- codigo aqui--> 
    <h1>Hola Mundo desde Bootstrap</h1>





    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
</html>"""
f=open("index.html","w")
f.write(texto)
f.close()


