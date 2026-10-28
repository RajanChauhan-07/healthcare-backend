
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from patients.models import Patient
from .models import Doctor, PatientDoctorMapping
from .serializers import DoctorSerializer
from .mapping_serializers import PatientDoctorMappingSerializer


# Doctor CRUD APIs
class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)


# Create and list patient-doctor mappings
class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user,
            doctor__user=self.request.user,
        ).select_related("patient", "doctor")

    def perform_create(self, serializer):
        patient = get_object_or_404(
            Patient,
            id=self.request.data.get("patient"),
            user=self.request.user,
        )
        doctor = get_object_or_404(
            Doctor,
            id=self.request.data.get("doctor"),
            user=self.request.user,
        )
        serializer.save(patient=patient, doctor=doctor)


# GET uses patient ID; DELETE uses mapping ID
class MappingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        patient = get_object_or_404(
            Patient,
            id=pk,
            user=request.user,
        )

        mappings = PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor__user=request.user,
        ).select_related("patient", "doctor")

        serializer = PatientDoctorMappingSerializer(
            mappings,
            many=True,
        )
        return Response(serializer.data)

    def delete(self, request, pk):
        mapping = get_object_or_404(
            PatientDoctorMapping.objects.filter(
                patient__user=request.user,
                doctor__user=request.user,
            ),
            id=pk,
        )

        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
