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
    <!-- Bootstrap core CSS -->
    <link href="../../dist/css/bootstrap.min.css" rel="stylesheet" >
    <link href="../../assets/css/docs.css" rel="stylesheet">
    <!-- icons Bootstrap -->
    <link rel="stylesheet" href="../../assets/icons/font/bootstrap-icons.css">
  </head>

  <body>
  
    <!-- Codigo aqui -->








    <!-- Bootstrap JS-->
    <script src="../../dist/js/bootstrap.bundle.min.js" ></script>
    <script src="https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js"></script>
    <script src="../../assets/js/docs.min.js"></script>

  </body>
</html>"""
f=open("index_offline.html","w")
f.write(texto)
f.close()


