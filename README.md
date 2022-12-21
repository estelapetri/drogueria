# drogueria
Luego de crear el repositorio en github y guardar en el los avances de los trabajos en clase,
Para finalizar el trabajo realice un clon de mi repositorio con el comando

git clone https://github.com/estelapetri/entrega-final.git .

donde, el path mencionado es la direccion de mi trabajo en github.
Agregue las dos class nuevas y todo lo necesario para hacerlas funcionar creando los foms, views, trmplates y urls
Para guardar los cambios definitivos realice la siguiente sucesion de comandos
git add .
git commit -m "entrega corregida"
git push origin main

En mi trabajo se puede realizar vistas de una lista de familiares, una lista de mascotas y una lista de vehiculos.

Para poder acceder a todos ellos desde una terminal bash ejecute el comando

python manage.py runserver

luego desde el navegador abrimos la pagina 
localhost:8000
aparecera el abm de familires, mascotas y vehiculos desde donde se podra listar el cotenido de la base ya creada,
cargar nuevas instancias, modificarlas o borrarlas