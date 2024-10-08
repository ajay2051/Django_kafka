from django.core.management import BaseCommand

from dj_kafka.kafka_consumer import start_consuming


class Command(BaseCommand):
    """
    Custom Management Command to consume Kafka messages
    """
    help = 'Starts consuming messages from Kafka'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting Kafka consumer...'))
        start_consuming()