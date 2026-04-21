from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Skill, Project
from .serializers import SkillSerializer, ProjectSerializer, ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        featured = self.request.query_params.get('featured')
        if featured == 'true':
            qs = qs.filter(is_featured=True)
        return qs


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ContactView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Send email notification
            try:
                send_mail(
                    subject=f"New message from {serializer.validated_data['name']}",
                    message=f"Name: {serializer.validated_data['name']}\n"
                            f"Email: {serializer.validated_data['email']}\n\n"
                            f"Message:\n{serializer.validated_data['message']}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_RECEIVER],
                    fail_silently=True,
                )
            except Exception:
                pass
            return Response(
                {'message': 'Message received! I will get back to you soon.'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    