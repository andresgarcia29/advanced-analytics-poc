## Parte 1 IAC.

En el path "./terraform" podrán encontrar el código que se utilizo para desplegar la infrastructura, creamos un módulo "./terraform/modules" llamado analytics donde agrupamos todos los componentes necesarios para el uso de la aplicación, tales como:

- Artifact Registry
- Cloud Run
- IAM configurations
- BigQuery dataset
- BigQuery tables

Y para desplegar el módulo usamos fases "./terraform/phases" que representan los diferentes ambientes de despliegue.

## Parte 2 Aplicaciones.

#### Parte 2.1

Dentro del folder "./apps/api" podemos observar el endpoint que levantamos para leer todos desde una base de datos de bigquery.

#### Parte 2.2

Para deployar la aplicación creamos una nueva versión de la misma y modificamos el cloud-run para que utilice el latest, el pipeline se puede encontrar en la siguiente ruta "./.github/workflows/api-build-and-push.yaml"

#### Parte 2.3

Creamos la aplicación dentro del path "./apps/ingester" para leer un queue y después insertar los datos a la tabla.

#### Parte 2.3

Diagrama:

#### Parte 2 comentarios.

- Se utilizo el patron de diseño Repository.
- Se utilizo la reocmendación de clean code separados entities, use cases, controllers.
- Se utilizo Docker y Docker-compose para el desarrollo
- Se agrego sistema de logging

#### Parte 2 Puntos de mejora.

- Agregar test unitarios en el código

## Parte 3 Pruebas de integración.

#### Parte 3.1

No se realizo, pero se podría hacer creando otro pipeline y ejecutando un comando para que corra una prueba donde se conecte directamente a la base de datos cree un par de registros y se verifique que se crearon correctamente en la base de datos.

#### Parte 3.2

- Crear todos los happy path cases que llevan conexión con la base de datos
- Simular una entrada de mensajes en la architectura pub-sub para ver que estan escribiendo correctamente

#### Parte 3.3

- Preparar por si el sistema escala a recibir más mensajes de los soportados
- Que los mensajes una vez procesados no se estén deplicando.
- Que los mensajes tengan un buen sistema de storage.
- Que los mensajes tengan replicas en diferntes zonas.
- Que los mensajes no tarden tanto en procesarse.

#### Parte 3.4

- Implementar un algoritmo para el balanceo de topicos
- Agregar un sistema de serialización para los mensajes
- Tener un sistema de re-intentos en caso de falla

## Parte 4 Métricas y monitoreo.

#### Parte 4.1

- Número de replicas de la aplicación corriendo
- Procesos activos
- Número de bytes in/out en el netowork

#### Parte 4.2

- Prometheus - Grafana
- Datadog
- ELK

Estás herramientas nos ayudarían a visualizar en dashboard métricas de nuestra aplicación hasta de cluster donde estemos utilizando las mismas.

#### Parte 4.3

En un cluster de kubernetes por ejemplo se instala un agente donde se estará recolectando métricas y guardando en una base de datos de series de tiempo.

#### Parte 4.4

La creación de los dashboard deberían estar controladas bajo el estandar de IAC.

#### Parte 4.5

- Falta de recursos

## Parte 5 Alertas

#### Parte 5.1

- El sistema usa más del 80% de los recursos
- El sistema tiene menos replicas de las esperadas.

#### Parte 5.1

Latencia:

Tiempo medio para procesar un mensaje desde su recepción de RabbitMQ hasta su escritura exitosa en BigQuery.
Latencia de la cola: Tiempo medio que un mensaje pasa en la cola de RabbitMQ antes de ser consumido por la aplicación.

Tasa de éxito:

Porcentaje de mensajes recibidos de RabbitMQ que se escriben con éxito en BigQuery.
Porcentaje de mensajes que se procesan sin errores o excepciones.

Tasa de errores:

Porcentaje de mensajes que fallan al intentar escribir en BigQuery.
Porcentaje de mensajes de RabbitMQ que generan errores al ser consumidos o procesados.

Volumen de tráfico:

Número total de mensajes recibidos de RabbitMQ en un intervalo de tiempo específico.
Número total de mensajes escritos en BigQuery en un intervalo de tiempo específico.

Retraso de la cola:

Número de mensajes no procesados en la cola de RabbitMQ.
Tiempo máximo que un mensaje ha estado esperando en la cola de RabbitMQ antes de ser consumido.

Eficiencia de recursos:

Uso promedio de CPU y memoria de la aplicación durante el procesamiento de los mensajes.
Uso de la red durante la transferencia de datos a BigQuery.

Durabilidad y Persistencia:

Porcentaje de mensajes que, una vez procesados, están garantizados para ser almacenados de manera duradera en BigQuery (en función de los mecanismos de confirmación y las políticas de reintentos).

Capacidad y escalabilidad

Número máximo de mensajes que la aplicación puede procesar por segundo sin degradación notable en la latencia.
Tiempo requerido para escalar y manejar picos de tráfico.
