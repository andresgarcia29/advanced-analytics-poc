import os
import logging

import pika

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def callback(ch, method, properties, body):
    """
    Callback que será llamado cuando se reciba un mensaje de la cola.
    """
    logger.info(f" [x] Recibido {body}")
    # Insertar registro a big query


def main():
    logger.info("Init")
    connection = pika.BlockingConnection(pika.URLParameters(os.getenv("RABBIT_MQ")))
    channel = connection.channel()

    queue_name = os.getenv("QUEUE_LISTENER_NAME")
    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    logger.info(f" [*] Esperando mensajes de {queue_name}.")
    channel.start_consuming()


if __name__ == "__main__":
    main()
