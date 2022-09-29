from PlayGroundEvent.models import Event, Ticket, BaseDateMixin, Company
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'date', 'organizer', 'sponsors', 'ticket_count'
        ]


class TicketSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        fields = [
            'event', 'price', 'user', 'vip', 'number',
        ]


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = [
            'title'
        ]

