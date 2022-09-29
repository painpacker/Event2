from django.shortcuts import render
from django.http import JsonResponse

from PlayGroundEvent.models import Ticket, Event, BaseDateMixin, Company
from rest_framework import viewsets
from rest_framework import permissions
from PlayGroundEvent.serializers import EventSerializer, TicketSerializer, CompanySerializer


def return_ticket(request, evid):
    ticket = Ticket.objects.get(pk=evid)
    return JsonResponse({
        'event': {"id": ticket.event_id},
        'price': ticket.price,
        'number': ticket.number,
    })


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]



