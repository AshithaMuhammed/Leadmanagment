from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView

from rest_framework.response import Response

from api.models import Lead

from api.serializers import LeadSerializer

from rest_framework import authentication,permissions

class BooksListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        context={"message":"listing all books"} #type dictionary

        #dictionary => json


        return Response(data=context)
    

    def post(self,request,*args,**kwargs):

        context={"message":"creating a new book object"}

        return Response(data=context)
    
class BookRetrieveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        context={"message":"fetach a specific book detail"}

        return Response(data=context)
    
    def put(self,request,*args,**kwargs):

        context={"message":"logic for updating a book"}

        return Response(data=context)
    
    def delete(self,request,*args,**kwargs):

        context={"message":"logic for deleting a book"}

        return Response(data=context)
    


# API enables communication between two software application


# http_request

# url:

# method:[GET,POST,PUT,PATCH,DELETE]

# Book

# headers

# json =>format for transferring data

# DRF 

# rest_framework>views>APIView

# rest_framework>response>Response =>python_native_type=>JSON

class LeadListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request,*args,**kwargs):

        # fetch all leads

        qs=Lead.objects.all()

        serializer_instance=LeadSerializer(qs,many=True) # conveying queryset to py native_type
    

        return Response(data=serializer_instance.data)
    

    def post(self,request,*args,**kwargs):

        serializer_instance=LeadSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)



class LeadRetrieveUpdateDestroy(APIView):
    
    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    serializer_class=LeadSerializer

    def get(self,request,*args,**kwargs):
        

        id=kwargs.get("pk")

        qs=Lead.objects.get(id=id)
        
        serializer_instance=self.serializer_class(qs)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Lead.objects.get(id=id).delete()

        return Response(data={"message":"deleted"})
    
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        lead_object=Lead.objects.get(id=id)

        serializer_instance=self.serializer_class(data=request.data,instance=lead_object)

        if serializer_instance.is_valid():

            serializer_instance.save() #update

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)

from django.db.models import Count
class LeadSummary(APIView):

    def get(self,request,*args,**kwargs):

        all_lead_count=Lead.objects.all().count()

        source_summary=Lead.objects.all().values("source").annotate(count=Count("source"))

        course_summary=Lead.objects.all().values("course").annotate(count=Count("course"))

        status_summary=Lead.objects.all().values("status").annotate(count=Count("status"))

        context={
            "total":all_lead_count,
            "source_summary":source_summary,
            "course_summary":course_summary,
            "status_summary":status_summary,

        }

        return Response(data=context)
    

#authenication and permissions

# credemtial: username,password basic authentication

#permissions=[allowany,isadminuser,isauthenticated,is authenticated reason only,]











        




