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
    <!-- Bootstrap CSS OFFLINE --> 
    <link href="file:///C:/bootstrap-5.3.0/css/bootstrap.min.css" rel="stylesheet" type="text/css" >
    <!-- icons Bootstrap -->
    <link rel="stylesheet" href="file:///C:/bootstrap-5.3.0/icons-main/font/bootstrap-icons.css">
  </head>

  <body>
  
    <!-- Codigo aqui -->
    <div class="d-flex align-items-center justify-content-center" style="height: 250px;">
      <span class="badge rounded-pill text-bg-primary">
        Hola mundo estoy usando Bootstrap
        <i class="bi bi-lightning-charge-fill"></i>
      </span>
    </div>



    <!-- Bootstrap JS OFFLINE -->
    <script src="file:///C:/bootstrap-5.3.0/js/bootstrap.bundle.min.js" 
    </script>
  </body>
</html>"""
f=open("index_offline.html","w")
f.write(texto)
f.close()


