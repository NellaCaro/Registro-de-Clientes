TÉCNICAS DE PROGRAMACIÓN - Trabajo Práctico Integrador 2023

Consideraciones Iniciales:

Dado el siguiente requerimiento realizar una aplicación en Python que emplee las estructuras básicas del Paradigma de Programación Estructurada:
- Funciones
- Estructuras de Control
- Estructuras de datos
- Manejo de Archivos de Texto.

Un supermercado ofrece a sus clientes la posibilidad de registrarse en su nomina de clientes a través de los siguientes medios: Pagina web, link de recomendación de un cliente ya registrado o mediante un grupo de WhatsApp.
Para el registro, los clientes deben completar un formulario con sus datos personales(DNI, nombre y apellido, domicilio, número de teléfono y dirección de mail). Los clientes registrados cuentan con un sistema de puntos con las siguientes características:
- Por cada afiliación de un nuevo cliente a través del link de recomendación de un cliente registrado, el cliente que recomienda recibe 500 puntos y el nuevo afiliado 200 puntos.
- Los clientes que se registran por medio del grupo de WhatsApp reciben de obsequio 50 puntos.
- Los clientes que se registran por medio de la pagina web reciben de obsequio 100 puntos.
- Con cada compra realizada por un cliente registrado suma 250 puntos.
  
Los clientes registrados se clasifican de la siguiente manera según su puntuación:
- Cliente Bronce: 50-1000 puntos.
- Cliente Plata: 1001-5000 puntos
- Clientes Oro: 5001 en adelante.
 
Finalmente, los clientes registrados cuentan con los siguientes beneficios:
- Clientes Bronce: 10% de descuento sobre el total del valor de cada compra.
- Clientes Plata: 15% de descuento sobre el total del valor de cada compra.
- Clientes Oro: 20% de descuento sobre el total del valor de cada compra
  
Además, los clientes Plata participan de un sorteo mensual de una canasta de productos básicos, mientras que los Clientes Oro participan de dos sorteos mensuales de la canasta de productos básicos y un adicional de un vale por $50.000 para realizar compras.
  
Funcionalidades de la Aplicación:
- Gestión de Clientes (Agregar, modificar, eliminar clientes)
- Gestión de Puntajes de clientes y clasificación de estos.
- Gestión de listas de clientes (clientes Bronce, Clientes Plata, Clientes Oro), para todos los casos se deberá generar el archivo Cliente_tipo.txt que muestre los siguientes datos: DNI, nombre y apellido, domicilio, email, medio de suscripción, puntaje actual, clasificación
